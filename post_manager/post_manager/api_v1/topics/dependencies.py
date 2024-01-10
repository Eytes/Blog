from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.topics import crud
from post_manager.api_v1.topics.excceptions import (
    TopicNotFoundByIdHTTPException,
    TopicNotFoundByNameHTTPException,
    TopicAlreadyExistsHTTPException,
)
from post_manager.api_v1.topics.schemas import TopicCreate
from post_manager.core.models import db_helper, Topic


async def get_topic_by_id(
    topic_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Topic:
    topic = await crud.get_by_id(session=session, topic_id=topic_id)
    if topic is None:
        raise TopicNotFoundByIdHTTPException(topic_id)
    return topic


async def get_topic_by_name(
    topic_name: str,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Topic:
    topic = await crud.get_by_name(session=session, name=topic_name)
    if topic is None:
        raise TopicNotFoundByNameHTTPException(topic_name)
    return topic


async def create_topic(
    topic: Annotated[TopicCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Topic:
    if await get_topic_by_name(session=session, topic_name=topic.name):
        raise TopicAlreadyExistsHTTPException
    return await crud.create(session=session, topic=topic)
