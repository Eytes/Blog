from typing import Annotated
from uuid import UUID

from fastapi import Depends, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    selectinload,
)

from post_manager.api_v1.authors.dependencies import get_author_by_id
from post_manager.api_v1.posts.dependencies import get_post_by_id
from post_manager.core.models import (
    Author,
    Post,
    db_helper,
)


async def get_posts_by_author_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> list[Post]:
    await get_author_by_id(
        author_id=author_id,
        session=session,
    )  # проверка существования автора
    statement = select(Post).where(Post.author_id == author_id)
    posts = await session.scalars(statement)
    return list(posts)


async def get_author_by_post_id(
    post_id: Annotated[UUID, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
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
