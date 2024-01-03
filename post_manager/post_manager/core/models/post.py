import datetime
from uuid import UUID

from sqlalchemy import (
    func,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from post_manager.core.models.base import Base


class Post(Base):
    author_id: Mapped[UUID] = mapped_column(
        ForeignKey("authors.id"),
        nullable=False,
        comment="id автора",
    )
    topic_id: Mapped[UUID] = mapped_column(
        ForeignKey("topics.id"),
        nullable=False,
        comment="id темы",
    )
    title: Mapped[str] = mapped_column(
        default="Без названия",
        server_default="Без названия",
        comment="Заголовок",
    )
    content: Mapped[str] = mapped_column(
        nullable=False,
        comment="содержимое",
    )
    creation_date: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
        comment="дата создания",
    )
    edit_date: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="дата последнего редактирования",
    )

    author: Mapped["Author"] = relationship(back_populates="posts")  # noqa: F821
    comments: Mapped[list["Comment"]] = relationship(  # noqa: F821
        back_populates="post"
    )
    topic: Mapped["Topic"] = relationship(back_populates="posts")  # noqa: F821
    likes: Mapped[list["Like"]] = relationship(back_populates="post")  # noqa: F821
