"""add column for team name

Revision ID: e69e70bea7e7
Revises: d7513ae5a00f
Create Date: 2025-01-21 03:07:22.889867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e69e70bea7e7'
down_revision: Union[str, None] = 'd7513ae5a00f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('teams', sa.Column('name', sa.String, nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('teams', 'name')
    pass
