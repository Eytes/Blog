from uuid import UUID

from post_manager.api_v1.exceptions import (
    NotFoundHTTPException,
    AlreadyExistsHTTPException,
)


class __TopicNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID | str):
        super().__init__()
        self.detail = f"Topic {identifier} not found!"


class TopicAlreadyExistsHTTPException(AlreadyExistsHTTPException):
    def __init__(self):
        super().__init__()
        self.detail = f"Topic already exists!"


class TopicNotFoundByIdHTTPException(__TopicNotFoundHTTPException):
    pass


class TopicNotFoundByNameHTTPException(__TopicNotFoundHTTPException):
    pass
