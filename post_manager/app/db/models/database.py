import os

from sqlalchemy.orm import DeclarativeBase


db_driver = os.getenv('DB_DRIVER')
db_username = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

print(f"{db_driver=}, {db_username=}, {db_password=}, {db_host=}, {db_name=}")

DATABASE_URL = f"{db_driver}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


class Base(DeclarativeBase):
    pass
