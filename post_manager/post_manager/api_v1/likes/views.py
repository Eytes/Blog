from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Body,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.likes.dependencies import (
    get_like_by_post_id_and_author_id,
    get_likes_amount_by_post_id,
)
from post_manager.api_v1.likes.schemas import Like, LikeCreate
from post_manager.core.models import db_helper

router = APIRouter(tags=["Likes"])


@router.get(
    "/post/{post_id}",
    response_model=int,
    status_code=status.HTTP_200_OK,
)
async def get_likes_amount_by_post_id(
    amount: Annotated[int, Depends(get_likes_amount_by_post_id)],
):
    return amount


@router.post(
    "/create",
    response_model=Like,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    like: Annotated[LikeCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    new_like = Like(**like.model_dump())
    session.add(like)
    await session.commit()
    await session.refresh(new_like)
    return new_like


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    like: Annotated[Like, Depends(get_like_by_post_id_and_author_id)],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
):
    await session.delete(like)
    await session.commit()
