"""adicionar novas tabelas

Revision ID: e6dc63a9aa30
Revises: fc98bdf1abae
Create Date: 2026-09-21 17:47:46.604410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6dc63a9aa30'
down_revision: Union[str, Sequence[str], None] = 'fc98bdf1abae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
