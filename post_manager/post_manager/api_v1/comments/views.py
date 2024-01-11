from typing import Annotated

from fastapi import APIRouter, status, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.comments import crud
from post_manager.api_v1.comments.dependencies import (
    get_comment_by_id,
    get_comments_by_post_id,
    get_comments_by_author_id,
    create_comment,
)
from post_manager.api_v1.comments.schemas import (
    Comment,
    CommentUpdate,
)
from post_manager.api_v1.posts.schemas import Post
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
    comments: Annotated[Post, Depends(get_comments_by_post_id)],
):
    """Получить комментарии поста по id поста"""
    return comments


@router.get(
    "/author/{author_id}/",
    response_model=list[Comment],
    status_code=status.HTTP_200_OK,
)
async def get_by_author_id(
    comments: Annotated[Post, Depends(get_comments_by_author_id)],
):
    """Получить комментарии автора по id автора"""
    return comments


@router.post(
    "/",
    response_model=Comment,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    comment: Annotated[Comment, Depends(create_comment)],
):
    """Создать комментарий для поста"""
    return comment


@router.patch(
    "/{comment_id}/",
    response_model=Comment,
)
async def update(
    comment_update: Annotated[CommentUpdate, Body],
    comment: Annotated[Comment, Depends(get_comment_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновить содержимое комментария"""
    return await crud.update(
        session=session,
        comment=comment,
        comment_update=comment_update,
        partial=True,
    )


@router.delete(
    "/{comment_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    comment: Annotated[Comment, Depends(get_comment_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Удаление комментария"""
    await crud.delete(session=session, comment=comment)
