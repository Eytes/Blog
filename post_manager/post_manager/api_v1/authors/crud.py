from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.schemas import (
    AuthorCreate,
    AuthorUpdate,
    AuthorUpdatePartial,
)
from post_manager.core.models import Author


async def get(session: AsyncSession) -> list[Author]:
    # TODO: добавить offset (каждые 10 пользователей, например)
    statement = select(Author).order_by(Author.id)
    authors = await session.execute(statement)
    return list(authors.scalars())


async def get_by_id(session: AsyncSession, author_id: UUID) -> Author | None:
    """Получение автора по id"""
    return await session.get(Author, author_id)


# TODO: Обработка ошибки IntegrityError (возникает при несоответствии условий данных)
async def create(session: AsyncSession, author: AuthorCreate) -> Author:
    """Создание нового автора"""
    new_author = Author(**author.model_dump())
    session.add(new_author)
    await session.commit()
    await session.refresh(
        new_author
    )  # для использования свежей версии автора, чтобы работать с актуальными данными
    return new_author


async def update(
    session: AsyncSession,
    author: Author,
    author_update: AuthorUpdate | AuthorUpdatePartial,
    partial: bool = False,
) -> Author:
    """Обновление данных об авторе"""
    for name, value in author_update.model_dump(exclude_unset=partial).items():
        setattr(author, name, value)
    await session.commit()
    return author


async def delete(
    session: AsyncSession,
    author: Author,
) -> None:
    """Удаление автора"""
    await session.delete(author)
    await session.commit()
