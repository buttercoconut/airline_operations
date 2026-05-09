"""Application configuration using Pydantic settings."""

from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    # Database URL
    database_url: PostgresDsn
    # Redis URL (optional, for caching)
    redis_url: str | None = None
    # Secret key for JWT or other auth (placeholder)
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
