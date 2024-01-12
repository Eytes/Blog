import datetime
from uuid import UUID

from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    author_id: UUID
    post_id: UUID


class CommentUpdate(CommentBase):
    pass


class CommentUpdatePartial(CommentBase):
    content: str | None = None


class Comment(CommentBase):
    id: UUID
    author_id: UUID
    post_id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
