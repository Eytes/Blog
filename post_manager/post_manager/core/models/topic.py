import datetime

from sqlalchemy import (
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from post_manager.core.models.base import Base


class Topic(Base):
    name: Mapped[str] = mapped_column(
        nullable=False,
        comment="Названание темы",
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

    # author: Mapped["Author"] = relationship(backref="posts")  # noqa: F821
    # comments: Mapped["Comment"] = relationship(back_populates="post")  # noqa: F821
