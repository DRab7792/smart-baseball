"""create players table

Revision ID: 90a786e6c666
Revises: 
Create Date: 2025-01-20 01:49:35.499516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90a786e6c666'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    CREATE TABLE players (
        player_id SERIAL PRIMARY KEY,    -- Unique identifier for the player
        mlb_id INT UNIQUE,               -- MLB player ID
        name VARCHAR(100) NOT NULL,      -- Player's name
        birth_date DATE,                 -- Player's date of birth
        position VARCHAR(50)             -- Player's position (e.g., pitcher, batter)
    );
    """
    op.create_table(
        'players',
        sa.Column('player_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('mlb_id', sa.Integer, unique=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('birth_date', sa.Date),
        sa.Column('position', sa.String(50))
    )
    pass


def downgrade() -> None:
    op.drop_table('players')
    pass
