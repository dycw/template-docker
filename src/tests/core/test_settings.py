from app.core.settings import SETTINGS
from app.core.settings import Settings


def test_settings() -> None:
    assert isinstance(SETTINGS, Settings)
