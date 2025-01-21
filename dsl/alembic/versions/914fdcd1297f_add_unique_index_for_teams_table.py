"""add unique index for teams table

Revision ID: 914fdcd1297f
Revises: e69e70bea7e7
Create Date: 2025-01-21 03:22:14.145713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '914fdcd1297f'
down_revision: Union[str, None] = 'e69e70bea7e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint('uq_teams', 'teams', ['rs_id', ])
    pass


def downgrade() -> None:
    op.drop_constraint('uq_teams', 'teams', type_='unique')
    pass
