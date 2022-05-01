lint:
  #!/usr/bin/env bash
  autoflake -ir --exclude=.venv --remove-all-unused-imports .
  isort .
  black .

local:
  poetry run uvicorn --host=localhost --port=8000 --reload app.main:app

test:
  #!/usr/bin/env bash
  export DOCKER_TOOLKIT=1
  docker build -f=docker/Dockerfile -t=foobar-test --target=test .
