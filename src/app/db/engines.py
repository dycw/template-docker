from collections.abc import Iterator

from beartype import beartype
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.settings import SETTINGS

SQLITE_ENGINE = create_engine(SETTINGS.DB_URL)
SessionLocal = sessionmaker(bind=SQLITE_ENGINE, autoflush=False, autocommit=False)


@beartype
def yield_sess() -> Iterator[Session]:  # pragma: no cover
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
