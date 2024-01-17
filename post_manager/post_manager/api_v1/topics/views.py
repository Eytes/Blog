from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.topics import crud
from post_manager.api_v1.topics.dependencies import (
    get_topic_by_id,
    create_topic,
    get_topic_by_name,
)
from post_manager.api_v1.topics.schemas import (
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
    "/name/{topic_name}/",
    response_model=Topic,
    status_code=status.HTTP_200_OK,
)
async def get_by_name(topic: Annotated[Topic, Depends(get_topic_by_name)]):
    """Получить данные о тематике по названию"""
    return topic


@router.post(
    "/",
    response_model=Topic,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    topic: Annotated[Topic, Depends(create_topic)],
):
    """Создание тематики постов"""
    return topic


@router.put(
    "/{topic_id}/",
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
    "/{topic_id}/",
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
