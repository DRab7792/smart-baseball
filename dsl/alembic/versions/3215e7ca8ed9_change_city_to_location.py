"""change city to location

Revision ID: 3215e7ca8ed9
Revises: 914fdcd1297f
Create Date: 2025-01-21 03:30:20.167958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3215e7ca8ed9'
down_revision: Union[str, None] = '914fdcd1297f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('teams', sa.Column('location', sa.String, nullable=True))

    op.drop_column('teams', 'state')
    op.drop_column('teams', 'city')
    pass


def downgrade() -> None:
    op.add_column('teams', sa.Column('city', sa.VARCHAR(length=100), nullable=True))
    op.add_column('teams', sa.Column('state', sa.VARCHAR(length=100), nullable=True))

    op.drop_column('teams', 'location')
    pass
