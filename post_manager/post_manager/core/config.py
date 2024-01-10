import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseModel):
    __POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    __POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    __POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    __POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    url: str = f"postgresql+asyncpg://{__POSTGRES_USER}:{__POSTGRES_PASSWORD}@{__POSTGRES_HOST}/{__POSTGRES_DB}"
    echo: bool = False


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DataBaseSettings = DataBaseSettings()


settings = Setting()
