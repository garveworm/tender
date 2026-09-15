from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str
    anthropic_api_key: str = ""
    model: str = ""
    max_iterations: int = 0
    max_tenders_searched: int = 0

    @property
    def migrating_db_url(self) -> str:
        return self.database_url.replace("+asyncpg", "+psycopg")


settings = Settings()
