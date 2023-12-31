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
    """Примесь в модель для добавления времени создания"""

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
    """Примесь в модель для добавления времени редактирования"""

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
    """Примесь в модель для добавления данных о связанном авторе"""

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
    """Примесь в модель для добавления данных о связанном посте"""

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


class TopicRelationMixin:
    """Примесь в модель для добавления данных о связанной теме поста"""

    _topic_id_comment: str = "id темы"
    _topic_id_nullable: bool = False
    _topic_back_populates: str | None = None

    @declared_attr
    def topic_id(cls) -> Mapped[UUID]:
        return mapped_column(
            ForeignKey("topics.id"),
            nullable=cls._topic_id_nullable,
            comment=cls._topic_id_comment,
        )

    @declared_attr
    def topic(cls) -> Mapped["Topic"]:  # noqa: F821
        return relationship(
            "Topic",
            back_populates=cls._topic_back_populates,
        )
