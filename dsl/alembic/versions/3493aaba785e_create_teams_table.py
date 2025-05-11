"""create teams table

Revision ID: 3493aaba785e
Revises: 90a786e6c666
Create Date: 2025-01-20 02:05:20.134215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3493aaba785e'
down_revision: Union[str, None] = '90a786e6c666'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Create an alembic upgrade migration based on the SQL provided.

    CREATE TABLE teams (
        team_id SERIAL PRIMARY KEY,       -- Unique identifier for the team
        mlb_id INT UNIQUE,                -- MLB team ID
        name VARCHAR(100) NOT NULL,       -- Team name
        abbreviation VARCHAR(10),         -- Team abbreviation (e.g., NYY for Yankees)
        league VARCHAR(50),               -- League (e.g., AL, NL)
        division VARCHAR(50)              -- Division (e.g., East, West, Central)
    );
    """
    op.create_table(
        'teams',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('year', sa.Integer, unique=True),
        sa.Column('abbreviation', sa.String(length=10)),
        sa.Column('league', sa.String(length=50)),
        sa.Column('franchise_id', sa.Integer),
        sa.Column('fg_id', sa.String(length=50)),
        sa.Column('br_id', sa.String(length=50)),
        sa.Column('rs_id', sa.String(length=50)),
        sa.Column('city', sa.String(length=100)),
        sa.Column('state', sa.String(length=50)),
        sa.Column('zip_code', sa.String(length=10)),
        sa.Column('stadium_id', sa.Integer)
    )

    op.create_index('ix_teams_franchise_id', 'teams', ['franchise_id'])
    op.create_index('ix_teams_fg_id', 'teams', ['fg_id'])
    op.create_index('ix_teams_br_id', 'teams', ['br_id'])
    op.create_index('ix_teams_rs_id', 'teams', ['rs_id'])
    op.create_index('ix_teams_stadium_id', 'teams', ['stadium_id'])
    pass


def downgrade() -> None:
    op.drop_table('teams')

    op.drop_index('ix_teams_franchise_id', table_name='teams')
    op.drop_index('ix_teams_fg_id', table_name='teams')
    op.drop_index('ix_teams_br_id', table_name='teams')
    op.drop_index('ix_teams_rs_id', table_name='teams')
    op.drop_index('ix_teams_stadium_id', table_name='teams')
    pass
