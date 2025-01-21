"""remove stadium id from teams table

Revision ID: 5e4e70280620
Revises: 3215e7ca8ed9
Create Date: 2025-01-21 03:47:36.444485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e4e70280620'
down_revision: Union[str, None] = '3215e7ca8ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('teams', 'stadium_id')
    pass


def downgrade() -> None:
    op.add_column('teams', sa.Column('stadium_id', sa.INTEGER(), nullable=True))
    op.create_index('ix_teams_stadium_id', 'teams', ['stadium_id'], unique=False)
    pass
