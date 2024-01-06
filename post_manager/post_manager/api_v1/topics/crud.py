from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.topics.schemas import (
    TopicCreate,
    TopicUpdate,
    TopicUpdatePartial,
)
from post_manager.core.models import Topic


async def get(session: AsyncSession) -> list[Topic]:
    """Получение всех тематик для потов"""
    statement = select(Topic).order_by(Topic.name)
    topics = await session.scalars(statement)
    return list(topics)


async def get_by_id(session: AsyncSession, topic_id: UUID) -> Topic | None:
    """Получение тематики по id"""
    return await session.get(Topic, topic_id)


async def create(
    session: AsyncSession,
    topic: TopicCreate,
) -> Topic:
    """Создание тематики для постов"""
    new_topic = Topic(**topic.model_dump())
    session.add(new_topic)
    await session.commit()
    await session.refresh(new_topic)
    return new_topic


async def update(
    session: AsyncSession,
    topic: Topic,
    topic_update: TopicUpdate | TopicUpdatePartial,
    partial: bool = False,
) -> Topic:
    """Обновление данных тематики"""
    for name, value in topic_update.model_dump(exclude_unset=partial).items():
        setattr(topic, name, value)
    await session.commit()
    return topic


async def delete(
    session: AsyncSession,
    topic: Topic,
) -> None:
    """Удаление тематики"""
    # TODO: сделать проверку, что нет постов по данной тематике
    await session.delete(topic)
    await session.commit()
