from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.dependencies import get_author_by_id
from post_manager.api_v1.posts import crud
from post_manager.api_v1.posts.exceptions import PostNotFoundByIdHTTPException
from post_manager.api_v1.posts.schemas import PostCreate
from post_manager.api_v1.topics.dependencies import get_topic_by_id
from post_manager.core.models import (
    db_helper,
    Post,
    Topic,
    Author,
)


async def get_post_by_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Post:
    """Получить пост по id"""
    post = await crud.get_by_id(session=session, post_id=post_id)
    if post is None:
        raise PostNotFoundByIdHTTPException(post_id)
    return post


async def get_topic_of_post_by_post_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Topic:
    """Получить тематику поста по id поста"""
    await get_post_by_id(session=session, post_id=post_id)
    return await crud.get_topic_by_post_id(session=session, post_id=post_id)


async def get_posts_by_author_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> list[Post]:
    """Получить посты определенного автора"""
    await get_author_by_id(author_id=author_id, session=session)
    return await crud.get_by_author_id(session=session, author_id=author_id)


async def get_author_by_post_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
    """Получить автора поста"""
    await get_post_by_id(session=session, post_id=post_id)
    return await crud.get_author_by_post_id(session=session, post_id=post_id)


async def create_post(
    new_post: Annotated[PostCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Создание поста"""
    await get_author_by_id(session=session, author_id=new_post.author_id)
    await get_topic_by_id(session=session, topic_id=new_post.topic_id)
    return await crud.create(session=session, post=new_post)
