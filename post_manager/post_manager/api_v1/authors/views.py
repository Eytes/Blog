from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors import crud
from post_manager.api_v1.authors.dependencies import (
    get_author_by_id,
    get_author_by_name,
    get_author_by_email,
)
from post_manager.api_v1.authors.schemas import (
    AuthorCreate,
    Author,
    AuthorUpdate,
    AuthorUpdatePartial,
)
from post_manager.core.models import db_helper

router = APIRouter(tags=["Authors"])


@router.post(
    "/create/",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_author: AuthorCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """Создание автора"""
    return await crud.create(session=session, author=new_author)


@router.put("/update/{author_id}/")
async def update(
    author_update: AuthorUpdate,
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """Обновление всех данных автора"""
    return await crud.update(
        session=session,
        author=author,
        author_update=author_update,
    )


@router.patch("/update/{author_id}/")
async def update_partial(
    author_update: AuthorUpdatePartial,
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """Обновление данных автора"""
    return await crud.update(
        session=session,
        author=author,
        author_update=author_update,
        partial=True,
    )


@router.get(
    "/id/{author_id}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(author: Author = Depends(get_author_by_id)):
    """Получение автора по id"""
    return author


@router.get(
    "/name/{name}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_name(author: Author = Depends(get_author_by_name)):
    """Получение автора по имени"""
    return author


@router.get(
    "/email/{email}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_name(author: Author = Depends(get_author_by_email)):
    """Получение автора по электронной почте"""
    return author


@router.get(
    "/",
    response_model=list[Author],
    status_code=status.HTTP_200_OK,
)
async def get(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    """Получение всех авторов"""
    # TODO: добавить offset (каждые 10 пользователей, например)
    return await crud.get(session)


@router.delete(
    "/id/{author_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    """Удаление автора"""
    await crud.delete(session=session, author=author)
