# app/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = os.getenv("DEBUG", False)
    database_url_source: str = os.getenv(
        "DATABASE_URL_SOURCE", "sqlite:///./source.db")
    database_url_destination: str = os.getenv(
        "DATABASE_URL_DESTINATION", "sqlite:///./destination.db")
    secret_key: str = os.getenv("SECRET_KEY", "mysecretkey")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    admin_username: str = os.getenv("ADMIN_USERNAME", "admin")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "adminpassword")
    access_token_expire_minutes: int = os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    # app_name: str = "FastAPI App"
    # debug: bool = False


settings = Settings()
