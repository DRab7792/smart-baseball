"""unique franchise names

Revision ID: 5dbbc23d5219
Revises: 03b0a939ca5e
Create Date: 2025-01-21 02:23:10.318314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dbbc23d5219'
down_revision: Union[str, None] = '03b0a939ca5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint('uq_franchise_name', 'franchises', ['name'])
    pass


def downgrade() -> None:
    op.drop_constraint('uq_franchise_name', 'franchises', type_='unique')
    pass
