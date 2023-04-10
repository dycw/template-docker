alembic-rev:
  alembic revision --autogenerate

alembic-up:
  alembic upgrade head

build:
  DOCKER_BUILDKIT=1 docker build -t=docker-template --target=production .

build-run:
  just build && just run

coverage:
  open .coverage/html/index.html

lint:
  DOCKER_BUILDKIT=1 docker build -t=docker-template --target=lint .

local:
  uvicorn --host=localhost --port=8000 --reload --app-dir=src app.main:app

run:
  APP_ENV=dev docker run docker-template

test:
  DOCKER_BUILDKIT=1 docker build -t=docker-template --target=test .
