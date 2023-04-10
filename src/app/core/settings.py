from typing import Any, Literal, cast

from typed_settings import default_loaders, load_settings, settings


@settings
class _EnvSettings:
    ENV: Literal["dev", "test", "prod"]


_ENV = load_settings(
    cast(Any, _EnvSettings), default_loaders("app", config_files=["pyproject.toml"])
).ENV


@settings
class Settings:
    DB_URL: str
    DEBUG: bool
    LOGGING_BACKTRACE: bool
    LOGGING_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    TITLE: str


SETTINGS = load_settings(
    cast(Any, Settings),
    default_loaders("app", ["pyproject.toml"], config_file_section=f"app_{_ENV}"),
)
