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


class Like(Base):
    post_id: Mapped[UUID] = mapped_column(
        ForeignKey("posts.id"),
        nullable=False,
        comment="id поста",
    )
    author_id: Mapped[UUID] = mapped_column(
        ForeignKey("authors.id"),
        nullable=False,
        comment="id автора",
    )
    creation_date: Mapped[datetime.datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
        nullable=False,
        comment="дата создания",
    )

    author: Mapped["Author"] = relationship(back_populates="likes")  # noqa: F821
    post: Mapped["Post"] = relationship(back_populates="likes")  # noqa: F821
