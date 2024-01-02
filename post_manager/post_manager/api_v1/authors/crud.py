from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.schemas import (
    AuthorCreate,
    AuthorUpdate,
)
from post_manager.core.models import Author


async def get_by_id(session: AsyncSession, author_id: UUID) -> Author | None:
    """Получение автора по id"""
    return await session.get(Author, author_id)


async def create(session: AsyncSession, author: AuthorCreate) -> Author:
    """Создание нового автора"""
    new_author = Author(**author.model_dump())
    session.add(new_author)
    await session.commit()
    await session.refresh(
        new_author
    )  # для использования свежей версии автора, чтобы работать с актуальными данными
    return new_author


async def update(session: AsyncSession, author_id: UUID, new_author_data: AuthorUpdate):
    """Обновление данных об авторе"""
    pass
