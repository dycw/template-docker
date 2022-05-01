from fastapi.testclient import TestClient
from pytest import fixture

from app.main import app


@fixture(scope="function")
def testclient():

    with TestClient(app) as client:
        # Application 'startup' handlers are called on entering the block.
        yield client
    # Application 'shutdown' handlers are called on exiting the block.
