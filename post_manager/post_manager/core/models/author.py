from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column,
)

from post_manager.core.models.base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    posts: Mapped["Post"] = relationship(back_populates="author")  # noqa: F821
    comments: Mapped["Comment"] = relationship(back_populates="author")  # noqa: F821
