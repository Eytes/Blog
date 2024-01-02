from uuid import UUID

from fastapi import APIRouter

from post_manager.api_v1.authors import crud
from post_manager.api_v1.authors.schemas import (
    AuthorCreate,
    AuthorUpdate,
    Author,
)

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)


@router.post("/create")
def create(new_author: AuthorCreate):
    """Создание автора"""
    # TODO: отправить запрос в БД на создание
    # TODO: обработать ответ от БД
    # TODO: выдать результат
    pass


@router.put("/update")
def update(new_author_data: AuthorUpdate):
    """Обновление данных автора"""
    # TODO: отправить запрос в БД на обновление
    # TODO: обработать ответ от БД
    # TODO: выдать результат
    pass


@router.get("/{author_id}")
async def get_by_id(session, author_id: UUID) -> Author:
    """Получение автора по id"""
    return await crud.get_by_id(
        session=session,
        author_id=author_id,
    )
