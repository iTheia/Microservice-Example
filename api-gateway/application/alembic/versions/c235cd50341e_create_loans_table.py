"""create_loans_table

Revision ID: c235cd50341e
Revises: 116d508ade0c
Create Date: 2024-03-25 14:11:14.853050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c235cd50341e'
down_revision: Union[str, None] = '116d508ade0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'loans',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('clients.id')),
        sa.Column('amount', sa.DECIMAL(15, 2)),
        sa.Column('start_date', sa.Date),
        sa.Column('end_date', sa.Date),
        sa.Column('interest_rate', sa.DECIMAL(5, 2)),
        sa.Column('status', sa.String(20)),
        sa.Column('account_id', sa.String),
    )


def downgrade():
    op.drop_table('loans')