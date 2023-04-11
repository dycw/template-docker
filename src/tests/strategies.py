from typing import Any

from beartype import beartype
from fastapi.testclient import TestClient
from hypothesis.strategies import composite
from utilities.hypothesis import lift_draw
from utilities.hypothesis.sqlalchemy import sqlite_engines

from app.db.engines import create_yield_sess, yield_sess
from app.db.schemas.all import create_tables
from app.main import create_app


@composite
@beartype
def clients(_draw: Any, /) -> TestClient:
    draw = lift_draw(_draw)
    engine = draw(sqlite_engines())
    create_tables(engine)
    app = create_app()
    app.dependency_overrides[yield_sess] = create_yield_sess(engine)
    return TestClient(app)
