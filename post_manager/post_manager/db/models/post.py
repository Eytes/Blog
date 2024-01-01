import uuid
from sqlalchemy import (
    Column,
    String,
    Integer,
    Uuid,
    TIMESTAMP,
    func,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from post_manager.db.models.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Uuid(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False)
    author_id = Column(Uuid(as_uuid=True), ForeignKey('authors.id'), nullable=False, comment='id автора')
    topic = Column(Integer, nullable=False, comment='id темы')
    content = Column(String, nullable=False, comment='содержимое')
    creation_date = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment='дата создания')
    edit_date = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment='дата последнего редактирования'
    )

    author = relationship("Author", backref='posts')
    comments = relationship("Comment", back_populates='post')
