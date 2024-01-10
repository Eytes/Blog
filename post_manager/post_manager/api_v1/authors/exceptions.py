from uuid import UUID

from pydantic import EmailStr

from post_manager.api_v1.exceptions import (
    NotFoundHTTPException,
    AlreadyExistsHTTPException,
)


class __AuthorNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID | EmailStr | str):
        super().__init__()
        self.detail = f"Author {identifier} not found!"


class AuthorAlreadyExistsHTTPException(AlreadyExistsHTTPException):
    def __init__(self):
        super().__init__()
        self.detail = "Name or email already exists!"


class AuthorNotFoundByIdHTTPException(__AuthorNotFoundHTTPException):
    pass


class AuthorNotFoundByNameHTTPException(__AuthorNotFoundHTTPException):
    pass


class AuthorNotFoundByEmailHTTPException(__AuthorNotFoundHTTPException):
    pass
