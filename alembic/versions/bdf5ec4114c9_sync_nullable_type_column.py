"""Sync nullable type column

Revision ID: bdf5ec4114c9
Revises: dbd3499e9890
Create Date: 2025-12-24 00:15:40.351053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdf5ec4114c9'
down_revision: Union[str, Sequence[str], None] = 'dbd3499e9890'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
