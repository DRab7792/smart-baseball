"""update_stadiums_table_with_unique_index

Revision ID: 0cfcb3cb40cd
Revises: d6fdc9294982
Create Date: 2025-05-11 05:08:32.579072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cfcb3cb40cd'
down_revision: Union[str, None] = 'd6fdc9294982'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the existing index first
    op.drop_index('ix_stadiums_rs_id', table_name='stadiums')
    
    # Create a unique constraint
    op.create_index('ix_stadiums_rs_id', 'stadiums', ['rs_id'], unique=True)
    pass


def downgrade() -> None:
    # Drop the unique constraint
    op.drop_index('ix_stadiums_rs_id', table_name='stadiums')
    
    # Recreate the non-unique index
    op.create_index('ix_stadiums_rs_id', 'stadiums', ['rs_id']) 
    pass