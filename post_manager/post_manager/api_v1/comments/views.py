from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, status, Depends, Path, Body
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1 import utils
from post_manager.api_v1.comments import crud
from post_manager.api_v1.comments.dependencies import get_comment_by_id
from post_manager.api_v1.comments.schemas import Comment, CommentCreate, CommentUpdate
from post_manager.core.models import db_helper

router = APIRouter(tags=["Comments"])


@router.get(
    "/{comment_id}/",
    response_model=Comment,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(comment: Annotated[Comment, Depends(get_comment_by_id)]):
    """Получить комментарий по id"""
    return comment


@router.get(
    "/post/{post_id}/",
    response_model=list[Comment],
    status_code=status.HTTP_200_OK,
)
async def get_by_post_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить комментарии поста по id поста"""
    return await utils.get_comments_by_post_id(session=session, post_id=post_id)


@router.get(
    "/author/{author_id}/",
    response_model=list[Comment],
    status_code=status.HTTP_200_OK,
)
async def get_by_post_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Получить комментарии автора по id автора"""
    return await utils.get_comments_by_author_id(session=session, author_id=author_id)


@router.post(
    "/create/",
    response_model=Comment,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    comment: Annotated[CommentCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создать комментарий для поста"""
    return await crud.create(session=session, comment=comment)


@router.patch(
    "/{comment_id}",
    response_model=Comment,
)
async def update(
    comment: Annotated[Comment, Depends(get_comment_by_id)],
    comment_update: Annotated[CommentUpdate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновить содержимое комментария"""
    return await crud.update(
        session=session,
        comment=comment,
        comment_update=comment_update,
    )
