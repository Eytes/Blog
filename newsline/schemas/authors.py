import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
)


class AuthorBase(BaseModel):
    name: str
    email: EmailStr


class AuthorCreate(AuthorBase):
    name: str
    email: EmailStr


class Author(AuthorBase):
    id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
