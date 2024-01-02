from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
)


class AuthorBase(BaseModel):
    name: str
    email: EmailStr


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorCreate):
    pass


class AuthorUpdatePartial(AuthorCreate):
    name: str | None = None
    email: EmailStr | None = None


class Author(AuthorBase):
    model_config = ConfigDict(
        from_attributes=True,
    )  # конфиг для конвертации объектов sqlalchemy в pydantic
    id: UUID
