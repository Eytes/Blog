import datetime
from uuid import UUID

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declared_attr,
    relationship,
)


class CreationDateMixin:
    _creation_date_comment: str = "дата создания"
    _creation_date_nullable: bool = False

    @declared_attr
    def creation_date(cls) -> Mapped[datetime.datetime]:
        return mapped_column(
            default=func.now(),
            server_default=func.now(),
            nullable=cls._creation_date_nullable,
            comment=cls._creation_date_comment,
        )


class EditDateMixin:
    _edit_date_comment: str = "дата последнего редактирования"
    _edit_date_nullable: bool = False

    @declared_attr
    def edit_date(cls) -> Mapped[datetime.datetime]:
        return mapped_column(
            default=func.now(),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=cls._edit_date_nullable,
            comment=cls._edit_date_comment,
        )


class AuthorRelationMixin:
    _author_id_comment: str = "id автора"
    _author_id_nullable: bool = False
    _author_back_populates: str | None = None

    @declared_attr
    def author_id(cls) -> Mapped[UUID]:
        return mapped_column(
            ForeignKey("authors.id"),
            nullable=cls._author_id_nullable,
            comment=cls._author_id_comment,
        )

    @declared_attr
    def author(cls) -> Mapped["Author"]:  # noqa: F821
        return relationship(
            "Author",
            back_populates=cls._author_back_populates,
        )


class PostRelationMixin:
    _post_id_comment: str = "id поста"
    _post_id_nullable: bool = False
    _post_back_populates: str | None = None

    @declared_attr
    def post_id(cls) -> Mapped[UUID]:
        return mapped_column(
            ForeignKey("posts.id"),
            nullable=cls._post_id_nullable,
            comment=cls._post_id_comment,
        )

    @declared_attr
    def post(cls) -> Mapped["Post"]:  # noqa: F821
        return relationship(
            "Post",
            back_populates=cls._post_back_populates,
        )
