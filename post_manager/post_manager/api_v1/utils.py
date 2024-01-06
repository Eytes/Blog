from typing import Annotated
from uuid import UUID

from fastapi import Depends, Path
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
    db_helper,
    Topic,
)


async def get_posts_by_author_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
) -> list[Post]:
    """Получить посты определенного автора"""
    await get_author_by_id(
        author_id=author_id,
        session=session,
    )  # проверка существования автора
    statement = select(Post).where(Post.author_id == author_id)
    posts = await session.scalars(statement)
    return list(posts)


async def get_posts_with_authors(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
):
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
    post_id: Annotated[UUID, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
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
    post_id: Annotated[UUID, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
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
