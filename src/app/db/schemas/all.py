from beartype import beartype
from sqlalchemy import Engine

from app.db.schemas import users
from app.db.schemas.base import Base

_ = [users]


@beartype
def create_tables(engine: Engine, /) -> None:
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)
