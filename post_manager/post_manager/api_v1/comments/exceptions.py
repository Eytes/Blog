from uuid import UUID

from post_manager.api_v1.exceptions import NotFoundHTTPException


class __CommentNotFoundHTTPException(NotFoundHTTPException):
    def __init__(self, identifier: UUID):
        super().__init__()
        self.detail = f"Comment {identifier} not found!"


class CommentNotFoundByIdHTTPException(__CommentNotFoundHTTPException):
    pass
