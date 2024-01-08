from typing import Annotated
from uuid import UUID

from fastapi import (
    APIRouter,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1 import utils
from post_manager.api_v1.topics import crud
from post_manager.api_v1.topics.dependencies import get_topic_by_id
from post_manager.api_v1.topics.schemas import (
    TopicCreate,
    TopicUpdate,
    TopicUpdatePartial,
    Topic,
)
from post_manager.core.models import db_helper

router = APIRouter(tags=["Topics"])


@router.get(
    "/",
    response_model=list[Topic],
    status_code=status.HTTP_200_OK,
)
async def get(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить все тематики постов"""
    return await crud.get(session)


@router.get(
    "/{topic_id}/",
    response_model=Topic,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(topic: Annotated[Topic, Depends(get_topic_by_id)]):
    """Получить тематику по id"""
    return topic


@router.get(
    "/post/{post_id}/",
    response_model=Topic,
    status_code=status.HTTP_200_OK,
)
async def get_by_post_id(
    post_id: UUID,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить тематику поста по id поста"""
    return await utils.get_topic_by_post_id(
        post_id=post_id,
        session=session,
    )


@router.post("/create/", response_model=Topic, status_code=status.HTTP_201_CREATED)
async def create(
    topic: TopicCreate,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создание тематики постов"""
    return await crud.create(session=session, topic=topic)


@router.put(
    "/update/{topic_id}",
    response_model=Topic,
)
async def update(
    topic_update: TopicUpdate,
    topic: Annotated[Topic, Depends(get_topic_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновление всех данных о тематике"""
    return await crud.update(
        session=session,
        topic=topic,
        topic_update=topic_update,
    )


@router.patch(
    "/update/{topic_id}",
    response_model=Topic,
)
async def update_partial(
    topic_update: TopicUpdatePartial,
    topic: Annotated[Topic, Depends(get_topic_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Частичное обновление данных о тематике"""
    return await crud.update(
        session=session,
        topic=topic,
        topic_update=topic_update,
        partial=True,
    )


@router.delete(
    "/{topic_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    topic: Annotated[Topic, Depends(get_topic_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> None:
    """Удаление тематики"""
    await crud.delete(session=session, topic=topic)
