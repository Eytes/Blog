from uuid import UUID

from pydantic import EmailStr

from post_manager.api_v1.exceptions import (
    NotFoundHTTPException,
)


class __TopicNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID | EmailStr | str):
        super().__init__()
        self.detail = f"Topic {identifier} not found!"


class TopicNotFoundByIdHTTPException(__TopicNotFoundHTTPException):
    pass
