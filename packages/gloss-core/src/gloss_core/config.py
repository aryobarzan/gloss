"""Application settings, read from environment variables / .env (prefix ``GLOSS_``)."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="GLOSS_", env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://gloss:gloss@localhost:5432/gloss"
    data_dir: Path = Path("./data")
    log_level: str = "INFO"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    contact_email: str | None = None

    @property
    def raw_dir(self) -> Path:
        return self.data_dir / "raw"

    @property
    def processed_dir(self) -> Path:
        return self.data_dir / "processed"


@lru_cache
def get_settings() -> Settings:
    return Settings()
