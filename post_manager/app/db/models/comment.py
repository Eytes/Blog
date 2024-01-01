import uuid
from sqlalchemy import (
    Column,
    String,
    Uuid,
    TIMESTAMP,
    func,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.db.models.database import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Uuid(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False)
    author_id = Column(Uuid(as_uuid=True), ForeignKey('authors.id'), nullable=False)
    post_id = Column(Uuid(as_uuid=True), ForeignKey('posts.id'), nullable=False)
    text = Column(String, nullable=False)
    creation_date = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='дата создания')
    edit_date = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment='дата последнего редактирования'
    )
    author = relationship("Author", backref='comments')
    post = relationship("Post", backref='comments')
