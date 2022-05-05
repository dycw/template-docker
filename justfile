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
  poetry run uvicorn --host=localhost --port=8000 --reload --app-dir=src \
  app.main:app

test:
  DOCKER_BUILDKIT=1 docker build -t=docker-template --target=test .
