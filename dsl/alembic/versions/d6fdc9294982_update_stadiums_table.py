"""update_stadiums_table

Revision ID: d6fdc9294982
Revises: 01a8bd4b5a8d
Create Date: 2025-05-11 05:04:01.467219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6fdc9294982'
down_revision: Union[str, None] = '01a8bd4b5a8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Convert open and close columns to dates
    op.alter_column('stadiums', 'open',
        type_=sa.Date(),
        postgresql_using="make_date(open, 1, 1)",
        existing_type=sa.Integer()
    )
    
    op.alter_column('stadiums', 'close', 
        type_=sa.Date(),
        postgresql_using="make_date(close, 12, 31)",
        existing_type=sa.Integer()
    )
    pass


def downgrade() -> None:
    op.alter_column('stadiums', 'close',
        type_=sa.Integer(),
        postgresql_using="EXTRACT(YEAR FROM close)",
        existing_type=sa.Date()
    )
    op.alter_column('stadiums', 'open',
        type_=sa.Integer(),
        postgresql_using="EXTRACT(YEAR FROM open)",
        existing_type=sa.Date()
    )
    pass