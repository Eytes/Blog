"""add creation date, edit date for author table and add post id for comment table

Revision ID: 827f86d829de
Revises: 8fefce677a6c
Create Date: 2024-01-03 17:13:25.985100

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "827f86d829de"
down_revision: Union[str, None] = "8fefce677a6c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "authors",
        sa.Column(
            "creation_date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата создания",
        ),
    )
    op.add_column(
        "authors",
        sa.Column(
            "edit_date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Дата последнего редактирования",
        ),
    )
    op.alter_column(
        "comments",
        "post_id",
        existing_type=sa.UUID(),
        comment="id поста",
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "comments",
        "post_id",
        existing_type=sa.UUID(),
        comment=None,
        existing_comment="id поста",
        existing_nullable=False,
    )
    op.drop_column("authors", "edit_date")
    op.drop_column("authors", "creation_date")
    # ### end Alembic commands ###
