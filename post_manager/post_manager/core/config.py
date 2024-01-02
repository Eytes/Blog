from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "postgresql+asyncpg://test:test@localhost:5431/test"
    db_echo: bool = True  # TODO: Заменить на False при публикации на сервере


settings = Setting()
