from uuid import UUID

from fastapi import HTTPException, status
from pydantic import EmailStr


class __NotFoundException(HTTPException):
    def __init__(self, identifier: UUID | EmailStr | str):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = f"Author {identifier} not found!"


class NotFoundByIdException(__NotFoundException):
    pass


class NotFoundByNameException(__NotFoundException):
    pass


class NotFoundByEmailException(__NotFoundException):
    pass
