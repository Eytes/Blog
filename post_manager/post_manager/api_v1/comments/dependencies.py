from typing import Annotated
from uuid import UUID

from fastapi import Depends, Path, Body
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.dependencies import get_author_by_id
from post_manager.api_v1.comments import crud
from post_manager.api_v1.comments.exceptions import CommentNotFoundByIdHTTPException
from post_manager.api_v1.comments.schemas import CommentCreate
from post_manager.api_v1.posts.dependencies import get_post_by_id
from post_manager.core.models import db_helper, Comment


async def get_comment_by_id(
    comment_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Comment:
    """Получить комментарий по id"""
    comment = await crud.get_by_id(session=session, comment_id=comment_id)
    if comment is None:
        raise CommentNotFoundByIdHTTPException(comment_id)
    return comment


async def get_comments_by_author_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> list[Comment]:
    """Получить комментарии автора по id автора"""
    await get_author_by_id(author_id=author_id, session=session)
    # TODO: сделать offset
    return await crud.get_by_author_id(session=session, author_id=author_id)


async def get_comments_by_post_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> list[Comment]:
    """Получить все комментарии поста по id поста"""
    await get_post_by_id(session=session, post_id=post_id)
    # TODO: добавить offset
    return await crud.get_by_post_id(session=session, post_id=post_id)


async def create_comment(
    new_comment: Annotated[CommentCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создать комментарий для поста"""
    await get_author_by_id(session=session, author_id=new_comment.author_id)
    await get_post_by_id(session=session, post_id=new_comment.post_id)
    return await crud.create(session=session, comment=new_comment)
