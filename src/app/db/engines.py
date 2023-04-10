from collections.abc import Callable, Iterator

from beartype import beartype
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

SQLITE_ENGINE = create_engine("sqlite:///db.sqlite")


@beartype
def create_yield_sess(engine: Engine, /) -> Callable[[], Iterator[Session]]:
    """Create a `yield_sess` iterator for a given engine."""
    sess_maker = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    def yield_sess() -> Iterator[Session]:
        sess = sess_maker()
        try:
            yield sess
        finally:
            sess.close()

    return yield_sess


yield_sess = create_yield_sess(SQLITE_ENGINE)
