# tests/core/test_config.py
from app.core.config import settings


def test_settings():
    assert settings.app_name == "FastAPI App"
    assert settings.debug == False  # Adjust based on your requirements
