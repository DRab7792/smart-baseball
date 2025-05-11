"""create_stadiums_table

Revision ID: 01a8bd4b5a8d
Revises: fcf088d18603
Create Date: 2025-05-11 04:27:28.787117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01a8bd4b5a8d'
down_revision: Union[str, None] = 'fcf088d18603'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'stadiums',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('nickname', sa.String),
        sa.Column('open', sa.Integer),
        sa.Column('close', sa.Integer),
        sa.Column('league', sa.String),
        sa.Column('notes', sa.String),
        sa.Column('parkalias', sa.String),
        sa.Column('rs_id', sa.String),
        sa.Column('parkname', sa.String),
        sa.Column('city', sa.String),
        sa.Column('state', sa.String),
        sa.Column('country', sa.String),
        sa.Column('mlb_lifetime', sa.Integer),
        sa.Column('seating_capacity', sa.Integer),
        sa.Column('first_deck_seating_rows', sa.Integer),
        sa.Column('mez_second_deck_seating_rows', sa.Integer),
        sa.Column('upper_deck_seating_rows', sa.Integer),
        sa.Column('lower_deck_overhang_pct', sa.Float),
        sa.Column('upper_deck_overhang_pct', sa.Float),
        sa.Column('fair_territory_sqft', sa.Float),
        sa.Column('foul_territory_sqft', sa.Float),
        sa.Column('lf_fence_height', sa.Integer),
        sa.Column('cf_fence_height', sa.Integer),
        sa.Column('rf_fence_height', sa.Integer),
        sa.Column('cf_orientation', sa.String),
        sa.Column('backstop', sa.Integer),
        sa.Column('left_field_distance', sa.Integer),
        sa.Column('left_center_distance', sa.Integer), 
        sa.Column('center_field_distance', sa.Integer),
        sa.Column('right_center_distance', sa.Integer),
        sa.Column('right_field_distance', sa.Integer)
    )
    op.create_index('ix_stadiums_rs_id', 'stadiums', ['rs_id'])
    pass


def downgrade() -> None:
    op.drop_table('stadiums')
    pass
