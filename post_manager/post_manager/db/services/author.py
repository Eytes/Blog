import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from post_manager.db.models.author import Author


async def add(session: AsyncSession, name: str, email: str) -> Author:
    """
    Добавляет в сессию нового автора
    """
    new_author = Author(name=name, email=email)
    session.add(new_author)
    return new_author


async def get_by_id(session: AsyncSession, author_id: uuid.UUID) -> tuple:
    """
    Получение автора по id
    """
    query = select(Author).filter_by(id=author_id)
    result = await session.execute(query)
    return result.fetchone().tuple()
