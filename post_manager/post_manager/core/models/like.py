from post_manager.core.models.base import Base
from post_manager.core.models.mixins import (
    CreationDateMixin,
    AuthorRelationMixin,
    PostRelationMixin,
)


class Like(Base, CreationDateMixin, AuthorRelationMixin, PostRelationMixin):
    _author_back_populates = "likes"
    _post_back_populates = "likes"
