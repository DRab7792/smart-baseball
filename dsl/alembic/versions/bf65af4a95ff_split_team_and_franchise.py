"""split team and franchise

Revision ID: bf65af4a95ff
Revises: 860d43edb66b
Create Date: 2025-01-20 18:10:34.172167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf65af4a95ff'
down_revision: Union[str, None] = '860d43edb66b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('franchise', 'franchises')

    op.drop_column('teams', 'zip_code')
    pass


def downgrade() -> None:
    op.rename_table('franchises', 'franchise')

    op.add_column('teams', sa.Column('zip_code', sa.VARCHAR(length=10), nullable=True))
    pass
