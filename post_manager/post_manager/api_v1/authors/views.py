from typing import Annotated
from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1 import utils
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
from post_manager.core.models import db_helper, Post

router = APIRouter(tags=["Authors"])


@router.get(
    "/",
    response_model=list[Author],
    status_code=status.HTTP_200_OK,
)
async def get(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получение всех авторов"""
    # TODO: добавить offset (каждые 10 пользователей, например)
    return await crud.get(session)


@router.get(
    "/{author_id}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(author: Annotated[Author, Depends(get_author_by_id)]):
    """Получение автора по id"""
    return author


@router.get(
    "/name/{name}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_name(author: Annotated[Author, Depends(get_author_by_name)]):
    """Получение автора по имени"""
    return author


@router.get(
    "/email/{email}/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_by_email(author: Annotated[Author, Depends(get_author_by_email)]):
    """Получение автора по электронной почте"""
    return author


@router.get(
    "/post/{post_id}",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_author_by_post_id(
    post_id: UUID,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить автора по id поста"""
    return await utils.get_author_by_post_id(
        session=session,
        post_id=post_id,
    )


@router.get(
    "/posts/{author_id}/",
    response_model=list[Post],
    status_code=status.HTTP_200_OK,
)
async def get_posts_by_author_id(
    author_id: UUID,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить посты автора по id автора"""
    return await utils.get_posts_by_author_id(
        session=session,
        author_id=author_id,
    )


@router.post(
    "/create/",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_author: AuthorCreate,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создание автора"""
    return await crud.create(session=session, author=new_author)


@router.put("/update/{author_id}/")
async def update(
    author_update: AuthorUpdate,
    author: Annotated[Author, Depends(get_author_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
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
    author: Annotated[Author, Depends(get_author_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновление данных автора"""
    return await crud.update(
        session=session,
        author=author,
        author_update=author_update,
        partial=True,
    )


@router.delete(
    "/{author_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    author: Annotated[Author, Depends(get_author_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> None:
    """Удаление автора"""
    await crud.delete(session=session, author=author)
