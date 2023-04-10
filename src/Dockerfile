# syntax=docker/dockerfile:1

# https://bit.ly/374AGW9 - Lighten your Python image with Docker multi-stage builds
# https://bit.ly/39upBi5 - Fast Docker Builds With Caching (Not Only) For Python
# https://bit.ly/3FcBF3m - Poetry managed Python FastAPI application with Docker multi-stage builds
# https://bit.ly/3MqoCAL - Docker python image with psycopg2 installed

#### base #####################################################################
# stage for preparing Python & environment variables
FROM python:3.11.3-slim as base

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
