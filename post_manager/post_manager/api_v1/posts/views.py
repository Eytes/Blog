from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.schemas import Author
from post_manager.api_v1.posts import crud
from post_manager.api_v1.posts.dependencies import (
    get_post_by_id,
    get_posts_by_author_id,
    get_author_by_post_id,
    get_topic_of_post_by_post_id,
    create_post,
)
from post_manager.api_v1.posts.schemas import (
    Post,
    PostUpdatePartial,
    PostUpdate,
)
from post_manager.api_v1.topics.schemas import Topic
from post_manager.core.models import db_helper

router = APIRouter(tags=["Posts"])


@router.get(
    "/author/{author_id}/",
    response_model=list[Post],
    status_code=status.HTTP_200_OK,
)
async def get_posts_by_author_id(
    posts: Annotated[Author, Depends(get_posts_by_author_id)],
):
    """Получить посты автора по id автора"""
    return posts


@router.get(
    "/{post_id}/author/",
    response_model=Author,
    status_code=status.HTTP_200_OK,
)
async def get_author_by_post_id(
    author: Annotated[Post, Depends(get_author_by_post_id)],
):
    """Получить автора по id поста"""
    return author


@router.get(
    "/{post_id}/topic/",
    response_model=Topic,
    status_code=status.HTTP_200_OK,
)
async def get_by_post_id(
    topic: Annotated[Topic, Depends(get_topic_of_post_by_post_id)],
):
    """Получить тематику поста по id поста"""
    return topic


@router.get(
    "/{post_id}/",
    response_model=Post,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(post: Annotated[Post, Depends(get_post_by_id)]):
    """Получение поста по id"""
    return post


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


@router.post(
    "/",
    response_model=Post,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    post: Annotated[Post, Depends(create_post)],
):
    """Создание поста"""
    return post


@router.put(
    "/{post_id}/",
    response_model=Post,
)
async def update(
    post_update: PostUpdate,
    post: Annotated[Post, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Обновление всех данных поста"""
    return await crud.update(
        session=session,
        post=post,
        post_update=post_update,
    )


@router.patch(
    "/{post_id}/",
    response_model=Post,
)
async def update_partial(
    post_update: PostUpdatePartial,
    post: Annotated[Post, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    """Частичное обновление данных поста"""
    return await crud.update(
        session=session,
        post=post,
        post_update=post_update,
        partial=True,
    )


@router.delete(
    "/{post_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    post: Annotated[Post, Depends(get_post_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> None:
    """Удаление поста"""
    await crud.delete(session=session, post=post)
