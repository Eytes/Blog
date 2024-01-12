from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.schemas import (
    AuthorCreate,
    AuthorUpdate,
    AuthorUpdatePartial,
)
from post_manager.core.models import Author


async def get(session: AsyncSession) -> list[Author]:
    # TODO: добавить offset (каждые 10 пользователей, например)
    statement = select(Author).order_by(Author.creation_date)
    authors = await session.execute(statement)
    return list(authors.scalars())


async def get_by_id(session: AsyncSession, author_id: UUID) -> Author | None:
    """Получение автора по id"""
    return await session.get(Author, author_id)


async def get_by_name(session: AsyncSession, name: str) -> Author | None:
    """Получение автора по имени"""
    statement = select(Author).where(Author.name == name)
    author: Author | None = await session.scalar(statement)
    return author


async def get_by_email(session: AsyncSession, email: EmailStr) -> Author | None:
    """Получение пользователя по email"""
    statement = select(Author).where(Author.email == email)
    # result: Result = await session.execute(statement)
    # author: Author | None = result.scalar_one_or_none()
    author: Author | None = await session.scalar(statement)
    return author


async def get_by_name_or_email(
    session: AsyncSession,
    email: EmailStr | None = None,
    name: str | None = None,
) -> Author | None:
    statement = select(Author).where(
        or_(
            Author.email == email,
            Author.name == name,
        )
    )
    author = await session.scalar(statement)
    return author


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
