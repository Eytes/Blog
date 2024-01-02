from uuid import (
    UUID,
    uuid4,
)

from sqlalchemy import (
    text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    mapped_column,
    Mapped,
)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=text(f"{uuid4()}"),
    )
