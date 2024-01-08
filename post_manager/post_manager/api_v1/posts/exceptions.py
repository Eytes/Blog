from uuid import UUID

from post_manager.api_v1.exceptions import (
    NotFoundHTTPException,
)


class __PostNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID):
        super().__init__()
        self.detail = f"Post {identifier} not found!"


class PostNotFoundByIdHTTPException(__PostNotFoundHTTPException):
    pass
