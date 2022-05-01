test:
  #!/usr/bin/env bash
  export DOCKER_TOOLKIT=1
  docker build -f=docker/Dockerfile -t=foobar-test --target=test .
