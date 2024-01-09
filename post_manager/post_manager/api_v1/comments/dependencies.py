from typing import Annotated
from uuid import UUID

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.comments import crud
from post_manager.api_v1.comments.exceptions import CommentNotFoundByIdHTTPException
from post_manager.core.models import db_helper, Comment


async def get_comment_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    comment_id: Annotated[UUID, Path],
) -> Comment:
    comment = await crud.get_by_id(session=session, comment_id=comment_id)
    if comment is None:
        raise CommentNotFoundByIdHTTPException(comment_id)
    return comment
