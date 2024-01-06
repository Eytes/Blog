from uuid import UUID

from pydantic import EmailStr

from post_manager.api_v1.exceptions import (
    NotFoundHTTPException,
)


class __PostNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID | EmailStr | str):
        super().__init__()
        self.detail = f"Post {identifier} not found!"


class PostNotFoundByIdHTTPException(__PostNotFoundHTTPException):
    pass


class PostNotFoundByNameHTTPException(__PostNotFoundHTTPException):
    pass


class PostNotFoundByEmailHTTPException(__PostNotFoundHTTPException):
    pass
