# syntax=docker/dockerfile:1

# https://bit.ly/374AGW9 - Lighten your Python image with Docker multi-stage builds
# https://bit.ly/39upBi5 - Fast Docker Builds With Caching (Not Only) For Python
# https://bit.ly/3FcBF3m - Poetry managed Python FastAPI application with Docker multi-stage builds
# https://bit.ly/3MqoCAL - Docker python image with psycopg2 installed

# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/

#### base #####################################################################
# stage for preparing Python & environment variables
FROM python:3.11.3-slim as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV VENV_PATH='/opt/venv'
ENV PATH="$PATH_VENV/bin:$PATH"

#### build ####################################################################
# stage for building dependencies
FROM base as build

# apt
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  curl \
  build-essential

# virtual environment
RUN python -m venv "$VENV_PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

#### development ##############################################################
# stage for development
# For example using docker-compose to mount local volume under /app
FROM base as development
ENV FASTAPI_ENV=development

# copy venv from `build` stage
RUN python -m venv "$VENV_PATH"
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# copy source code
WORKDIR /app
COPY . .

# copy entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT /entrypoint.sh $0 $@
CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=8000", "main:app"]

#### lint #####################################################################
# 'lint' stage runs black and isort
# running in check mode means build will fail if any linting errors occur
# FROM development AS lint
# RUN black --check -q src
# RUN ruff check src
# CMD ["tail", "-f", "/dev/null"]

#### test #####################################################################
# 'test' stage runs our unit tests with pytest and coverage
# FROM development AS test
# RUN pytest -nauto src

#### production ###############################################################
# 'production' stage uses the clean 'base' stage and copies in only our
# runtime deps that were installed in the 'build'
FROM base as production
ENV FASTAPI_ENV=production

COPY --from=build "$VENV_PATH" "$VENV_PATH"
COPY ./docker/gunicorn_conf.py /gunicorn_conf.py

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


COPY ./src /src
WORKDIR /src

ENTRYPOINT /entrypoint.sh $0 $@
CMD [ \
  "gunicorn", \
  "--worker-class uvicorn.workers.UvicornWorker", \
  "--config /gunicorn_conf.py", \
  "app.main:app" ]
