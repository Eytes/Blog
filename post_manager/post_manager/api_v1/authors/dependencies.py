from typing import Annotated
from uuid import UUID

from fastapi import (
    Path,
    Depends,
    Body,
)
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.authors import crud
from post_manager.api_v1.authors.exceptions import (
    AuthorNotFoundByIdHTTPException,
    AuthorNotFoundByNameHTTPException,
    AuthorNotFoundByEmailHTTPException,
    AuthorAlreadyExistsHTTPException,
)
from post_manager.api_v1.authors.schemas import AuthorCreate
from post_manager.core.models import (
    db_helper,
    Author,
)


async def get_author_by_id(
    author_id: Annotated[UUID, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
    author = await crud.get_by_id(
        author_id=author_id,
        session=session,
    )
    if author is None:
        raise AuthorNotFoundByIdHTTPException(author_id)
    return author


async def get_author_by_name(
    name: Annotated[str, Path],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
    author = await crud.get_by_name(
        session=session,
        name=name,
    )
    if author is None:
        raise AuthorNotFoundByNameHTTPException(name)
    return author


async def get_author_by_email(
    email: Annotated[EmailStr, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
    author = await crud.get_by_email(
        session=session,
        email=email,
    )
    if author is None:
        raise AuthorNotFoundByEmailHTTPException(email)
    return author


async def create_author(
    author: Annotated[AuthorCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
) -> Author:
    if await crud.get_by_name_or_email(
        session=session,
        email=author.email,
        name=author.name,
    ):
        raise AuthorAlreadyExistsHTTPException
    return await crud.create(session=session, author=author)
