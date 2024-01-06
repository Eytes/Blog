import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str
    topic_id: UUID


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostUpdatePartial(PostBase):
    title: str | None = None
    content: str | None = None
    topic_id: UUID | None = None


class Post(BaseModel):
    """Схема данных с полной информацией о посте"""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    author_id: UUID
    topic_id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
