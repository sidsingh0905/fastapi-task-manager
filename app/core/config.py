from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "info"

    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
