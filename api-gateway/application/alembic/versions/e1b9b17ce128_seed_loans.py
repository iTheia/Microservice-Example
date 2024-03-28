"""seed_loans

Revision ID: e1b9b17ce128
Revises: c8fd2d76e554
Create Date: 2024-03-25 14:55:03.645063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1b9b17ce128'
down_revision: Union[str, None] = 'c8fd2d76e554'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.execute("""
        INSERT INTO loans (client_id, amount, start_date, end_date, interest_rate, status, account_id)
        VALUES
            (1, 1000, '2024-03-23', '2024-06-23', 5.0, 'active', '6600c7733cbe0eafbed475c8'),
            (2, 1000, '2024-03-23', '2024-06-23', 5.0, 'active', '6600c7733cbe0eafbed475c8'),
            (3, 1000, '2024-03-23', '2024-06-23', 5.0, 'active', '6600c7733cbe0eafbed475c8'),
            (1, 2000, '2024-03-23', '2024-06-23', 1.0, 'closed', '6600c7733cbe0eafbed475c8'),
            (2, 2000, '2024-03-23', '2024-06-23', 2.0, 'closed', '6600c7733cbe0eafbed475c8')
    """)

def downgrade():
    pass  # No action needed for downgrade
