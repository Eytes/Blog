from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    selectinload,
    joinedload,
)

from post_manager.api_v1.authors.dependencies import get_author_by_id
from post_manager.api_v1.posts.dependencies import get_post_by_id
from post_manager.core.models import (
    Author,
    Post,
    Topic,
)


async def get_posts_by_author_id(
    author_id: UUID,
    session: AsyncSession,
) -> list[Post]:
    """Получить посты определенного автора"""
    await get_author_by_id(
        author_id=author_id,
        session=session,
    )  # проверка существования автора
    statement = select(Post).where(Post.author_id == author_id)
    posts = await session.scalars(statement)
    return list(posts)


async def get_posts_with_authors(session: AsyncSession):
    """Получить посты и их авторов"""
    statement = (
        select(Post)
        .options(
            joinedload(Post.author),
        )
        .order_by(Post.creation_date)
    )
    posts = await session.scalars(statement)
    return list(posts)


async def get_author_by_post_id(
    post_id: UUID,
    session: AsyncSession,
) -> Author:
    """Получить автора поста"""
    await get_post_by_id(
        session=session,
        post_id=post_id,
    )  # проверка существования поста
    statement = (
        select(Author)
        .options(
            selectinload(Author.posts),
        )
        .where(Post.id == post_id)
    )
    author = await session.scalar(statement)
    return author


async def get_topic_by_post_id(
    post_id: UUID,
    session: AsyncSession,
) -> Topic:
    """Получить тематику поста"""
    await get_post_by_id(
        session=session,
        post_id=post_id,
    )
    statement = (
        select(Topic)
        .options(
            selectinload(Topic.posts),
        )
        .where(Post.id == post_id)
    )
    topic = await session.scalar(statement)
    return topic
