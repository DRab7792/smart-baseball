"""empty message

Revision ID: df6e315e3d17
Revises: 5e4e70280620
Create Date: 2025-05-05 02:58:29.957804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df6e315e3d17'
down_revision: Union[str, None] = '5e4e70280620'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('franchises', sa.Column('lh_id', sa.String(length=3), nullable=True))
    op.create_index('ix_franchises_lh_id', 'franchises', ['lh_id'], unique=True)
    pass


def downgrade() -> None:
    op.drop_index('ix_franchises_lh_id', table_name='franchises')
    op.drop_column('franchises', 'lh_id')
    pass
