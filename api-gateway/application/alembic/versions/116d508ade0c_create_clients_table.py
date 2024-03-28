"""create_clients_table

Revision ID: 116d508ade0c
Revises:
Create Date: 2024-03-25 14:08:38.538427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '116d508ade0c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clients',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('lastname', sa.String),
        sa.Column('account_id', sa.String),
        sa.Column('email', sa.String),
        sa.Column('phone', sa.String),
        sa.Column('is_deleted', sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table('clients')