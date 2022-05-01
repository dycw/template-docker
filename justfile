build:
  DOCKER_BUILDKIT=1 docker build -f=docker/Dockerfile -t=docker-template --target=production .

lint:
  #!/usr/bin/env bash
  autoflake -ir --exclude=.venv --remove-all-unused-imports .
  isort .
  black -q .

lint-d:
  DOCKER_BUILDKIT=1 docker build -f=docker/Dockerfile -t=docker-template --target=lint .

local:
  poetry run uvicorn --host=localhost --port=8000 --reload app.main:app

test:
  DOCKER_BUILDKIT=1 docker build -f=docker/Dockerfile -t=docker-template --target=test .
