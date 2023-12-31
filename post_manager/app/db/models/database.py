import os
import typing

import sqlalchemy
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs,
)
from sqlalchemy.orm import DeclarativeBase

db_driver = os.getenv('DB_DRIVER')
db_client = os.getenv('DB_CLIENT')
db_username = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')


class Base(AsyncAttrs, DeclarativeBase):
    pass


DATABASE_URL = f"{db_driver}+{db_client}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> typing.AsyncGenerator:
    async with async_session() as session:
        yield session


async def drop_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def create_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
