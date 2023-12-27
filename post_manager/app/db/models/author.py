import uuid
from sqlalchemy import (
    Column,
    String,
    Integer,
    Uuid,
    TIMESTAMP,
    func,
)
from sqlalchemy.orm import relationship

from app.db.models.database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Uuid(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)

    posts = relationship("Post", back_populates='author')
