from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Model config used to configure the behavior of Pydantic models.
    # It allows you to customize various aspects of model validation,
    # serialization, and other features.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    def get_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # JWT
    JWT_SECRET_KEY: str


settings = Settings()
