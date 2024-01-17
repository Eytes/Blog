import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
)


class TopicBase(BaseModel):
    name: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
