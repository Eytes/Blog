from uuid import UUID, uuid4
from fastapi import APIRouter

from post_manager.app.schemas.author import (
    CreateAuthor,
    UpdateAuthor,
    Author,
)

router = APIRouter(
    prefix="/authors",
    tags=["Author"],
)


@router.post("/create")
def create(new_author: CreateAuthor):
    """
    Эндпоинт для создания автора
    """
    # TODO: отправить запрос в БД на создание
    # TODO: обработать ответ от БД
    # TODO: выдать результат
    pass


@router.put("/update")
def update(new_author_data: UpdateAuthor):
    """
    Эндпоинт обновления данных автора
    """
    # TODO: отправить запрос в БД на обновление
    # TODO: обработать ответ от БД
    # TODO: выдать результат
    pass


@router.get("/{author_id}")
def get(author_id: UUID) -> Author:
    """
    Получение автора по id
    """
    # TODO: отправить запрос в БД для получение автора
    # TODO: обработать ответ от БД
    # TODO: выдать результат
    pass
