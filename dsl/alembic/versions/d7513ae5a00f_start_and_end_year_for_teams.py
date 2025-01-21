"""start and end year for teams

Revision ID: d7513ae5a00f
Revises: 5dbbc23d5219
Create Date: 2025-01-21 02:54:48.933316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7513ae5a00f'
down_revision: Union[str, None] = '5dbbc23d5219'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('teams', 'year')
    op.add_column('teams', sa.Column('start_year', sa.Integer, nullable=True))
    op.add_column('teams', sa.Column('end_year', sa.Integer, nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('teams', 'end_year')
    op.drop_column('teams', 'start_year')
    op.add_column('teams', sa.Column('year', sa.Integer, nullable=True))
    pass
