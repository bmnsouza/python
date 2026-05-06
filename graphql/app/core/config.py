from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database Oracle
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_service: str

    # Benchmark
    enable_benchmark: bool = False

    # Configuração para carregar do .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
