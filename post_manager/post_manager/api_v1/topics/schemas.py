import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TopicBase(BaseModel):
    name: str


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicBase):
    pass


class TopicUpdatePartial(TopicBase):
    name: str | None = None


class Topic(TopicBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
