from typing import Annotated
from uuid import UUID

from fastapi import Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors.dependencies import get_author_by_id
from post_manager.api_v1.likes import crud
from post_manager.api_v1.posts.dependencies import get_post_by_id
from post_manager.core.models import db_helper, Like


async def get_like_by_post_id_and_author_id(
    author_id: Annotated[UUID, Body],
    post_id: Annotated[UUID, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Like:
    await get_author_by_id(session=session, author_id=author_id)
    await get_post_by_id(session=session, post_id=post_id)
    return await crud.get_by_post_id_and_author_id(
        author_id=author_id,
        post_id=post_id,
        session=session,
    )


async def get_likes_amount_by_post_id(
    post_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> int:
    await get_post_by_id(session=session, post_id=post_id)
    return await crud.get_likes_amount_by_post_id(
        post_id=post_id,
        session=session,
    )
