from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
)


class AuthorBase(BaseModel):
    name: str
    email: EmailStr


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: UUID
