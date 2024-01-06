from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.topics import crud
from post_manager.api_v1.topics.excceptions import TopicNotFoundByIdHTTPException
from post_manager.api_v1.topics.schemas import Topic
from post_manager.core.models import db_helper


async def get_topic_by_id(
    topic_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Topic:
    topic = await crud.get_by_id(session=session, topic_id=topic_id)
    if topic is None:
        raise TopicNotFoundByIdHTTPException(topic_id)
    return topic
