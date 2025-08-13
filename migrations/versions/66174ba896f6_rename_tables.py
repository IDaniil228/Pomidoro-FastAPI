"""rename_tables

Revision ID: 66174ba896f6
Revises: 89c60777ff52
Create Date: 2025-05-19 02:03:12.479152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66174ba896f6'
down_revision: Union[str, None] = '89c60777ff52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.rename_table('Users', 'UserProfile')  # Новое название

def downgrade():
    op.rename_table('UserProfile', 'Users')
