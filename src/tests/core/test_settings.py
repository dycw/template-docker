from app.core.settings import SETTINGS, Settings


def test_settings() -> None:
    assert isinstance(SETTINGS, Settings)
