from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from post_manager.core.models.base import Base
from post_manager.core.models.mixins import (
    CreationDateMixin,
    EditDateMixin,
    IdMixin,
)


class Author(
    Base,
    IdMixin,
    CreationDateMixin,
    EditDateMixin,
):
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    posts: Mapped[list["Post"]] = relationship(  # noqa: F821
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    comments: Mapped[list["Comment"]] = relationship(  # noqa: F821
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    likes: Mapped[list["Like"]] = relationship(  # noqa: F821
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
