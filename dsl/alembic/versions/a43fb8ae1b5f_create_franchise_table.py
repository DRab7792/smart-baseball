"""create franchise table

Revision ID: a43fb8ae1b5f
Revises: e600857531bd
Create Date: 2025-01-20 02:33:13.945304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a43fb8ae1b5f'
down_revision: Union[str, None] = '3493aaba785e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'franchise',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('start_year', sa.Integer, nullable=True),
        sa.Column('end_year', sa.Integer, nullable=True)
    )
    pass


def downgrade() -> None:
    op.drop_table('franchise')
    pass
