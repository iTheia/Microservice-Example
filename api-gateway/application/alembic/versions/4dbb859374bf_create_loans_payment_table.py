"""create_loans_payment_table

Revision ID: 4dbb859374bf
Revises: c235cd50341e
Create Date: 2024-03-25 14:14:01.830661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dbb859374bf'
down_revision: Union[str, None] = 'c235cd50341e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'loans_payment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('loan_id', sa.Integer, sa.ForeignKey('loans.id')),
        sa.Column('amount', sa.DECIMAL(15, 2)),
        sa.Column('account_id', sa.String),
    )


def downgrade():
    op.drop_table('loans')