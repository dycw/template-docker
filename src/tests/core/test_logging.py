from logging import getLogger

from pytest import raises


def test_logging() -> None:
    logger = getLogger("uvicorn")
    logger.info("test")


def test_logging_invalid_level() -> None:
    uvicorn = getLogger("uvicorn")
    with raises(ValueError, match="Level '999' does not exist"):
        uvicorn.log(999, "test")
