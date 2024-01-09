from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from post_manager.api_v1.likes.schemas import LikeCreate
from post_manager.core.models import Like, Post


async def get_by_post_id_and_author_id(
    author_id: UUID,
    post_id: UUID,
    session: AsyncSession,
) -> Like:
    statement = (
        select(Like).where(Like.author_id == author_id).where(Like.post_id == post_id)
    )
    like = await session.scalar(statement)
    return like


async def get_likes_amount_by_post_id(session: AsyncSession, post_id: UUID) -> int:
    """Получить кол-во лайков под постом"""
    table_alias = (
        select(Like)
        .join(Post)
        .options(joinedload(Like.post))
        .where(Like.post_id == post_id)
    ).alias()
    statement = select(func.count()).select_from(table_alias)
    amount_of_likes = await session.scalar(statement)
    return amount_of_likes


async def create(
    session: AsyncSession,
    like: LikeCreate,
) -> Like:
    """Создание лайка под постом от определенного автора"""
    new_like = Like(**like.model_dump())
    session.add(new_like)
    await session.commit()
    await session.refresh(new_like)
    return new_like


async def delete(session: AsyncSession, like: Like) -> None:
    """Удаление лайка"""
    await session.delete(like)
    await session.commit()
