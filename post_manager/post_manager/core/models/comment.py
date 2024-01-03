from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from post_manager.core.models.base import Base
from post_manager.core.models.mixins import (
    CreationDateMixin,
    EditDateMixin,
    AuthorRelationMixin,
    PostRelationMixin,
)


class Comment(
    Base,
    CreationDateMixin,
    EditDateMixin,
    AuthorRelationMixin,
    PostRelationMixin,
):
    _author_back_populates = "comments"
    _post_back_populates = "comments"

    content: Mapped[str] = mapped_column(nullable=False)
