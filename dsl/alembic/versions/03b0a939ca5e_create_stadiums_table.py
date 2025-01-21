"""create stadiums table

Revision ID: 03b0a939ca5e
Revises: bf65af4a95ff
Create Date: 2025-01-20 18:13:46.528481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03b0a939ca5e'
down_revision: Union[str, None] = 'bf65af4a95ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
