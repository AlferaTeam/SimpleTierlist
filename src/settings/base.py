from typing import Dict, Tuple

from pydantic import BaseModel, BaseSettings
from pydantic_settings import SettingsConfigDict


class LoggingConfig(BaseModel):
    LEVEL: str = "DEBUG"
    PATH: str = "logs/app.log"


class DatabaseConfig(BaseModel):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "postgres"
    DB_PORT: int = 5432
    DB_MODELS: Tuple[str] = ("src.models", "aerich.models")

    @property
    def url(self):
        return f"asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class DiscordClient(BaseModel):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URL: str = ""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
    TITLE: str = "CISTiersAPI"
    DESCRIPTION: str | None = None
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    API_PREFIX: str | None = "/api"
    DOCS_URL: str | None = "/docs"
    OPENAPI_URL: str | None = "/openapi.json"
    REDOC_URL: str | None = "/redoc"
    OPENAPI_PREFIX: str = ""

    logging: LoggingConfig = LoggingConfig
    db: DatabaseConfig = DatabaseConfig
    discord: DiscordClient = DiscordClient

    @property
    def set_app_attributes(self) -> Dict[str, str | bool | None]:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
