from typing import Dict, Tuple

from pydantic import BaseSettings, validator


class LoggingConfig(BaseSettings):
    LEVEL: str = "DEBUG"
    PATH: str = "logs/app.log"

    class Config:
        env_prefix = "LOG_"


class DatabaseConfig(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_MODELS: Tuple[str, ...] = ("src.models", "aerich.models")

    class Config:
        env_prefix = "DB_"

    @property
    def url(self) -> str:
        return f"asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @validator("DB_PORT")
    def validate_port(cls, value):
        if not (1024 <= value <= 65535):
            raise ValueError("DB_PORT must be between 1024 and 65535.")
        return value


class DiscordClient(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URL: str = "http://localhost:8000/callback"

    class Config:
        env_prefix = "DISCORD_"


class AppSettings(BaseSettings):
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

    logging: LoggingConfig = LoggingConfig()
    db: DatabaseConfig = DatabaseConfig()
    discord: DiscordClient = DiscordClient()

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def app_attributes(self) -> Dict[str, str | bool | None]:
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
