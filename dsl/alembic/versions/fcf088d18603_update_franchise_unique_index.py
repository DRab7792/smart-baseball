"""update_franchise_unique_index

Revision ID: fcf088d18603
Revises: df6e315e3d17
Create Date: 2025-05-05 16:39:50.226797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcf088d18603'
down_revision: Union[str, None] = 'df6e315e3d17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop existing unique constraint on name column
    op.drop_constraint('uq_franchise_name', 'franchises', type_='unique')
    
    # Create new unique constraint on lh_id column
    op.create_unique_constraint('uq_franchise_lh_id', 'franchises', ['lh_id'])
    pass


def downgrade() -> None:
    # Drop unique constraint on lh_id column
    op.drop_constraint('uq_franchise_lh_id', 'franchises', type_='unique')
    
    # Recreate unique constraint on name column
    op.create_unique_constraint('uq_franchise_name', 'franchises', ['name'])
    pass
