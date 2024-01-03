from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseModel):
    url: str = "postgresql+asyncpg://test:test@localhost:5431/test"
    echo: bool = True  # TODO: Заменить на False при публикации на сервере


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DataBaseSettings = DataBaseSettings()


settings = Setting()
