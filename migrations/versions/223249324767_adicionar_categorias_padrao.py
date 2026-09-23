"""adicionar categorias padrao

Revision ID: 223249324767
Revises: e6dc63a9aa30
Create Date: 2026-09-23 08:23:26.997635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '223249324767'
down_revision: Union[str, Sequence[str], None] = 'e6dc63a9aa30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        INSERT INTO categorias (nome_categoria)
        VALUES ('alimentação'), ('transporte'), ('saúde'), ('educação'), ('lazer'), ('salário'), ('outros')
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        DELETE FROM categorias
        WHERE usuario_id_fk IS NULL
        AND nome_categoria IN ('alimentação', 'transporte', 'saúde', 'educação', 'lazer', 'salário', 'outros')
    """)