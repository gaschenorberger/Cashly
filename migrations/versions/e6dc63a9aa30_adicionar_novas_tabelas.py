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
    op.create_table(
        "usuarios",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("senha_hash", sa.String(length=255), nullable=False),
        sa.Column("ativo", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column("criado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("atualizado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )
    op.create_table(
        "categorias",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("usuario_id_fk", sa.BigInteger(), nullable=True),
        sa.Column("nome_categoria", sa.String(length=100), nullable=False),
        sa.Column("criado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("atualizado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["usuario_id_fk"], ["usuarios.id"], name="fk_categorias_usuario", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "transacoes",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("usuario_id_fk", sa.BigInteger(), nullable=False),
        sa.Column("categoria_id_fk", sa.BigInteger(), nullable=False),
        sa.Column("nome_transacao", sa.String(length=255), nullable=False),
        sa.Column("valor", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column("tipo_transacao", sa.String(length=10), nullable=False),
        sa.Column("data_transacao", sa.Date(), nullable=False),
        sa.Column("observacao", sa.Text(), nullable=True),
        sa.Column("criado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("atualizado_em", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("valor > 0", name="chk_transacoes_valor_positivo"),
        sa.CheckConstraint("tipo_transacao IN ('entrada', 'saida')", name="chk_transacoes_tipo"),
        sa.ForeignKeyConstraint(["categoria_id_fk"], ["categorias.id"], name="fk_transacoes_categoria", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["usuario_id_fk"], ["usuarios.id"], name="fk_transacoes_usuario", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("transacoes")
    op.drop_table("categorias")
    op.drop_table("usuarios")
