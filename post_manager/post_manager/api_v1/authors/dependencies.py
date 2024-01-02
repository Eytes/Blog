from typing import Annotated
from uuid import UUID

from fastapi import (
    Path,
    HTTPException,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors import crud
from post_manager.core.models import (
    db_helper,
    Author,
)


async def get_author_by_id(
    author_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Author:
    author = await crud.get_by_id(
        author_id=author_id,
        session=session,
    )
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author {author_id} not found!",
        )
    return author
