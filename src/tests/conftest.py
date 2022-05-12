from collections.abc import Callable, Iterator
from pathlib import Path

from beartype import beartype
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.engines import yield_sess
from app.db.schemas.all import create_tables
from app.main import create_app


@fixture()
@beartype
def engine(tmp_path: Path) -> Engine:
    engine = create_engine(f"sqlite:///{tmp_path}/db.sqlite")
    create_tables(engine)
    return engine


@fixture()
@beartype
def yield_test_sess(engine: Engine) -> Callable[[], Iterator[Session]]:
    TestSession = sessionmaker(  # noqa: N806
        bind=engine, autoflush=False, autocommit=False
    )

    def yield_test_sess() -> Iterator[Session]:
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    return yield_test_sess


@fixture()
@beartype
def app(yield_test_sess: Callable[[], Iterator[Session]]) -> FastAPI:
    app = create_app()
    app.dependency_overrides[yield_sess] = yield_test_sess
    return app


@fixture()
@beartype
def test_client(app: FastAPI) -> TestClient:
    return TestClient(app)
