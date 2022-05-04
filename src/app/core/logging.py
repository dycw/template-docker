from logging import Handler
from logging import LogRecord
from logging import __file__ as logging_file
from logging import currentframe
from types import FrameType
from typing import cast

from loguru import logger


class InterceptHandler(Handler):
    def emit(self, record: LogRecord) -> None:  # pragma: no cover
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
