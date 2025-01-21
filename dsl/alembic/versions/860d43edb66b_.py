"""empty message

Revision ID: 860d43edb66b
Revises: 62bff900f040, a43fb8ae1b5f
Create Date: 2025-01-20 18:10:06.016605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '860d43edb66b'
down_revision: Union[str, None] = ('62bff900f040', 'a43fb8ae1b5f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
