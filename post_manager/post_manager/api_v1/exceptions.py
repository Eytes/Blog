from fastapi import HTTPException, status


class NotFoundHTTPException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND


class AlreadyExistsHTTPException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
