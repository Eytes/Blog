from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.posts.schemas import (
    PostCreate,
    PostUpdate,
    PostUpdatePartial,
)
from post_manager.core.models import Post


async def get(session: AsyncSession) -> list[Post]:
    """Получение всех постов"""
    # TODO: добавить offset (каждые 10 пользователей, например)
    statement = select(Post).order_by(Post.id)
    result = await session.execute(statement)
    return list(result.scalars())


async def get_by_id(session: AsyncSession, post_id: UUID) -> Post | None:
    """Получить пост по id"""
    return await session.get(Post, post_id)


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
