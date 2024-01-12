from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from post_manager.api_v1.comments.schemas import (
    CommentCreate,
    CommentUpdate,
)
from post_manager.core.models import Comment


async def get_by_id(session: AsyncSession, comment_id: UUID) -> Comment | None:
    """Получить комментарий по id"""
    return await session.get(Comment, comment_id)


async def get_by_post_id(session: AsyncSession, post_id: UUID) -> list[Comment]:
    """Получить комментарии по id поста"""
    # TODO: добавить offset
    statement = select(Comment).where(Comment.post_id == post_id).order_by(Comment.creation_date)
    return list(await session.scalars(statement))


async def get_by_author_id(session: AsyncSession, author_id: UUID) -> list[Comment]:
    """Получить комментарии автора по id автора"""
    # TODO: добавить offset
    statement = select(Comment).where(Comment.author_id == author_id)
    return list(await session.scalars(statement))


async def create(session: AsyncSession, comment: CommentCreate) -> Comment:
    """Создание комментария"""
    new_comment = Comment(**comment.model_dump())
    session.add(new_comment)
    await session.commit()
    await session.refresh(new_comment)
    return new_comment


async def update(
    session: AsyncSession,
    comment: Comment,
    comment_update: CommentUpdate,
    partial: bool = False,
) -> Comment:
    """Обновление комментария"""
    for name, value in comment_update.model_dump(exclude_unset=partial).items():
        setattr(comment, name, value)
    await session.commit()
    return comment


async def delete(session: AsyncSession, comment: Comment) -> None:
    """Удаление комментария"""
    await session.delete(comment)
    await session.commit()
