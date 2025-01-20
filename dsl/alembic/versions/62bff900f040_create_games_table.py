"""create games table

Revision ID: 62bff900f040
Revises: 3493aaba785e
Create Date: 2025-01-20 02:07:54.862205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62bff900f040'
down_revision: Union[str, None] = '3493aaba785e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Create an alembic upgrade migration based on the SQL provided.

    CREATE TABLE games (
        game_id SERIAL PRIMARY KEY,       -- Unique identifier for the game
        mlb_id INT UNIQUE,                -- MLB game ID
        game_date DATE NOT NULL,          -- Date of the game
        home_team_id INT REFERENCES teams(team_id),  -- Home team
        away_team_id INT REFERENCES teams(team_id),  -- Away team
        home_score INT,                   -- Final score for the home team
        away_score INT                    -- Final score for the away team
    );
    """
    op.create_table(
        'games',
        sa.Column('game_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('mlb_id', sa.Integer, unique=True),
        sa.Column('game_date', sa.Date, nullable=False),
        sa.Column('home_team_id', sa.Integer, sa.ForeignKey('teams.team_id')),
        sa.Column('away_team_id', sa.Integer, sa.ForeignKey('teams.team_id')),
        sa.Column('home_score', sa.Integer),
        sa.Column('away_score', sa.Integer)
    )
    pass


def downgrade() -> None:
    op.drop_table('games')
    pass
