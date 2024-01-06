from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.posts import crud
from post_manager.api_v1.posts.exceptions import PostNotFoundByIdHTTPException
from post_manager.api_v1.posts.schemas import Post
from post_manager.core.models import db_helper


async def get_post_by_id(
    post_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Post:
    post = await crud.get_by_id(session=session, post_id=post_id)
    if post is None:
        raise PostNotFoundByIdHTTPException(post_id)
    return post
