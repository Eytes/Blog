from typing import Annotated
from uuid import UUID

from fastapi import (
    APIRouter,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1 import utils
from post_manager.api_v1.posts import crud
from post_manager.api_v1.posts.dependencies import get_post_by_id
from post_manager.api_v1.posts.schemas import (
    Post,
    PostCreate,
    PostUpdatePartial,
    PostUpdate,
)
from post_manager.core.models import db_helper

router = APIRouter(tags=["Posts"])


@router.get(
    "/",
    response_model=list[Post],
)
async def get(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получение всех постов"""
    # TODO: добавить offset (каждые 10 пользователей, например)
    return await crud.get(session)


@router.get(
    "/{post_id}/",
    response_model=Post,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(post: Annotated[Post, Depends(get_post_by_id)]):
    """Получение поста по id"""
    return post


@router.get(
    "/author/{author_id}/",
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
    response_model=Post,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_post: PostCreate,
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создание поста"""
    return await crud.create(session=session, post=new_post)


@router.put(
    "/update/{post_id}",
    response_model=Post,
)
async def update(
    post_update: PostUpdate,
    post: Annotated[Post, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновление всех данных поста"""
    return crud.update(
        session=session,
        post=post,
        post_update=post_update,
    )


@router.patch(
    "/update/{post_id}",
    response_model=Post,
)
async def update_partial(
    post_update: PostUpdatePartial,
    post: Annotated[Post, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Частичное обновление данных поста"""
    return crud.update(
        session=session,
        post=post,
        post_update=post_update,
        partial=True,
    )
