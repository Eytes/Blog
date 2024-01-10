from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from post_manager.api_v1.posts.schemas import (
    PostCreate,
    PostUpdate,
    PostUpdatePartial,
)
from post_manager.core.models import Post, Topic, Author


async def get(session: AsyncSession) -> list[Post]:
    """Получение всех постов"""
    # TODO: добавить offset (каждые 10 пользователей, например)
    statement = select(Post).order_by(Post.id)
    result = await session.execute(statement)
    return list(result.scalars())


async def get_by_id(session: AsyncSession, post_id: UUID) -> Post | None:
    """Получить пост по id"""
    return await session.get(Post, post_id)


async def get_topic_by_post_id(session: AsyncSession, post_id: UUID) -> Topic | None:
    """Получить тематику поста по id поста"""
    statement = (
        select(Topic)
        .options(
            selectinload(Topic.posts),
        )
        .where(Post.id == post_id)
    )
    topic = await session.scalar(statement)
    return topic


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


async def get_by_author_id(
    author_id: UUID,
    session: AsyncSession,
) -> list[Post]:
    """Получить посты определенного автора"""
    statement = select(Post).where(Post.author_id == author_id)
    posts = await session.scalars(statement)
    return list(posts)


async def get_author_by_post_id(
    post_id: UUID,
    session: AsyncSession,
) -> Author:
    """Получить автора поста"""
    statement = (
        select(Author)
        .join(Post)
        .options(
            selectinload(Author.posts),
        )
        .where(Post.id == post_id)
    )
    author = await session.scalar(statement)
    return author


async def create(session: AsyncSession, post: PostCreate) -> Post:
    """Создание нового поста"""
    new_post = Post(**post.model_dump())
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


async def update(
    session: AsyncSession,
    post: Post,
    post_update: PostUpdate | PostUpdatePartial,
    partial: bool = False,
) -> Post:
    """Обновление данных поста"""
    for name, value in post_update.model_dump(exclude_unset=partial).items():
        setattr(post, name, value)
    await session.commit()
    return post


async def delete(session: AsyncSession, post: Post) -> None:
    """Удаление поста"""
    await session.delete(post)
    await session.commit()
