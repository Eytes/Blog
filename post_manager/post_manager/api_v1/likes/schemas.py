import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LikeBase(BaseModel):
    author_id: UUID
    post_id: UUID


class LikeCreate(LikeBase):
    pass


class Like(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    author_id: UUID
    post_id: UUID
    creation_date: datetime.datetime
