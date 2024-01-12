import datetime
from uuid import UUID

from pydantic import BaseModel


class Post(BaseModel):
    id: UUID
    author_id: UUID
    title: str
    content: str
    topic_id: UUID
    creation_date: datetime.datetime
    edit_date: datetime.datetime
