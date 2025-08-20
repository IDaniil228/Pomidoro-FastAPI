"""delete access_token in UserProfile

Revision ID: 6367d70564de
Revises: b2256a50b708
Create Date: 2025-08-14 00:07:16.229437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6367d70564de'
down_revision: Union[str, None] = 'b2256a50b708'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
