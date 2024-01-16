import datetime
from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    author_id: UUID
    title: str
    content: str
    topic_id: UUID


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
