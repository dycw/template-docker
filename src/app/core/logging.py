from logging import Handler, LogRecord, basicConfig, currentframe
from logging import __file__ as logging_file
from pathlib import Path
from types import FrameType
from typing import cast

from beartype import beartype
from loguru import logger

from app.core.settings import SETTINGS


@beartype
def configure_logging() -> None:
    logger.remove()
    log_path = Path.cwd().joinpath("app.log")
    _ = logger.add(
        log_path,
        level=SETTINGS.LOGGING_LEVEL,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level:8} | {message}",
        enqueue=True,
        backtrace=SETTINGS.LOGGING_BACKTRACE,
        rotation="10 MB",
        retention="10 Days",
        compression="zip",
        serialize=False,
    )


class InterceptHandler(Handler):
    @beartype
    def emit(self, record: LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = currentframe(), 2
        while frame.f_code.co_filename == logging_file:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


basicConfig(handlers=[InterceptHandler()], level=0, force=True)
