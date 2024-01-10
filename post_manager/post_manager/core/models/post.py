from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from post_manager.core.models.base import Base
from post_manager.core.models.mixins import (
    AuthorRelationMixin,
    CreationDateMixin,
    EditDateMixin,
    TopicRelationMixin,
    IdMixin,
)


class Post(
    Base,
    IdMixin,
    AuthorRelationMixin,
    TopicRelationMixin,
    CreationDateMixin,
    EditDateMixin,
):
    _author_back_populates = "posts"
    _topic_back_populates = "posts"

    title: Mapped[str] = mapped_column(
        default="Без названия",
        server_default="Без названия",
        comment="Заголовок",
    )
    content: Mapped[str] = mapped_column(
        nullable=False,
        comment="Содержимое",
    )
    # TODO: добавить кол-во лайков отдельным полем

    comments: Mapped[list["Comment"]] = relationship(  # noqa: F821
        back_populates="post",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    likes: Mapped[list["Like"]] = relationship(  # noqa: F821
        back_populates="post",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
