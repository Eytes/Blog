from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from post_manager.core.models.base import Base
from post_manager.core.models.mixins import (
    CreationDateMixin,
    EditDateMixin,
)


class Topic(
    Base,
    CreationDateMixin,
    EditDateMixin,
):
    name: Mapped[str] = mapped_column(
        nullable=False,
        comment="Название темы",
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="topic")  # noqa: F821
