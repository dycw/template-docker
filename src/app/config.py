from functools import lru_cache
from logging import getLogger
from typing import cast

from beartype import beartype
from pydantic import AnyUrl, BaseSettings

log = getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = cast(bool, 0)
    database_url: AnyUrl = cast(AnyUrl, None)


@lru_cache
@beartype
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
