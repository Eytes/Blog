import os
import typing

from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs,
)
from sqlalchemy.orm import DeclarativeBase


load_dotenv()
__db_driver = os.getenv('DB_DRIVER')
__db_client = os.getenv('DB_CLIENT')
__db_username = os.getenv('DB_USER')
__db_password = os.getenv('DB_PASSWORD')
__db_host = os.getenv('DB_HOST')
__db_port = os.getenv('DB_PORT')
__db_name = os.getenv('DB_NAME')


class Base(AsyncAttrs, DeclarativeBase):
    pass


DATABASE_URL = f"{__db_driver}+{__db_client}://{__db_username}:{__db_password}@{__db_host}:{__db_port}/{__db_name}"
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
