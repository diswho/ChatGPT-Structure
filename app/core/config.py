from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = ""
    PROJECT_NAME: str = ""
    DATABASE_URL_INTERNAL: str = ""
    DATABASE_URL_EXTERNAL: str = ""
    BACKEND_CORS_ORIGINS: str = ""
    FIRST_SUPERUSER: str = ""
    FIRST_SUPERUSER_PASSWORD: str = ""

settings = Settings()
