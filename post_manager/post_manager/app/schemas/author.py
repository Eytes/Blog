from uuid import UUID
from typing import Annotated
from annotated_types import (
    MaxLen,
    MinLen,
)
from pydantic import (
    BaseModel,
    EmailStr,
)


class Author(BaseModel):
    id: UUID
    name: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr


class CreateAuthor(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr


class UpdateAuthor(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(20)]
    email: EmailStr
