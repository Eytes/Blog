from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseModel):
    url: str = "postgresql+asyncpg://eytes:qwerty@postgres/blog"
    # echo: bool = True  # TODO: Заменить на False при публикации на сервере
    echo: bool = False


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DataBaseSettings = DataBaseSettings()


settings = Setting()
