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
    Comment,
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
    # TODO: добавить offset
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


async def get_comments_by_post_id(
    post_id: UUID,
    session: AsyncSession,
) -> list[Comment]:
    """Получить все комментарии поста по id поста"""
    await get_post_by_id(
        session=session,
        post_id=post_id,
    )  # проверка существования поста
    # TODO: добавить offset
    statement = select(Comment).where(Comment.post_id == post_id)
    comments = await session.scalars(statement)
    return list(comments)


async def get_comments_by_author_id(
    author_id: UUID,
    session: AsyncSession,
) -> list[Comment]:
    """Получить комментарии автора по id автора"""
    await get_author_by_id(author_id=author_id, session=session)
    # TODO: сделать offset
    statement = select(Comment).where(Comment.author_id == author_id)
    comments = await session.scalars(statement)
    return list(comments)
