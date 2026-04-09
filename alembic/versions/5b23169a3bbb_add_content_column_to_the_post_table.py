"""Add content column to the post table

Revision ID: 5b23169a3bbb
Revises: 661597292bce
Create Date: 2026-04-07 20:12:19.149194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b23169a3bbb'
down_revision: Union[str, Sequence[str], None] = '661597292bce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
