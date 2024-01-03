from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from post_manager.core.models.base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="author")  # noqa: F821
    comments: Mapped[list["Comment"]] = relationship(  # noqa: F821
        back_populates="author"
    )
    likes: Mapped[list["Like"]] = relationship(back_populates="author")  # noqa: F821
