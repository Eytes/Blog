from typing import Annotated
from uuid import UUID

from fastapi import (
    Path,
    Depends,
)
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors import crud
from post_manager.api_v1.exeptions import (
    NotFoundByIdException,
    NotFoundByNameException,
    NotFoundByEmailException,
)
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
        raise NotFoundByIdException(author_id)
    return author


async def get_author_by_name(
    name: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Author:
    author = await crud.get_by_name(
        session=session,
        name=name,
    )
    if author is None:
        raise NotFoundByNameException(name)
    return author


async def get_author_by_email(
    email: EmailStr,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Author:
    author = await crud.get_by_email(
        session=session,
        email=email,
    )
    if author is None:
        raise NotFoundByEmailException(email)
    return author
