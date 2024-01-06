from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    selectinload,
)

from post_manager.core.models import (
    Author,
    Post,
)


async def get_posts_by_author_id(session: AsyncSession, author_id: UUID) -> list[Post]:
    statement = select(Post).where(Post.author_id == author_id)
    posts = await session.scalars(statement)
    return list(posts)


async def get_author_by_post_id(session: AsyncSession, post_id: UUID) -> Author:
    statement = (
        select(Author)
        .options(
            selectinload(Author.posts),
        )
        .where(Post.id == post_id)
    )
    author = await session.scalar(statement)
    return author
