from fastapi import APIRouter

from post_manager.app.schemas.author import (
    CreateAuthor,
    UpdateAuthor,
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
    pass


@router.put("/update")
def update(new_author_data: UpdateAuthor):
    """
    Эндпоинт обновления данных автора
    """
    pass
