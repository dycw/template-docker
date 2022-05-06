from typing import Literal

from typed_settings import load
from typed_settings import settings


@settings
class _EnvSettings:
    ENV: Literal["dev", "test", "prod"]


_ENV = load(_EnvSettings, "app", config_files=["pyproject.toml"]).ENV


@settings
class Settings:
    DB_URL: str
    DEBUG: bool
    LOGGING_BACKTRACE: bool
    LOGGING_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    TITLE: str


SETTINGS = load(
    Settings,
    "app",
    config_files=["pyproject.toml"],
    config_file_section=f"app_{_ENV}",
)
