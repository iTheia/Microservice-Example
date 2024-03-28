"""seed_clients

Revision ID: c8fd2d76e554
Revises: 4dbb859374bf
Create Date: 2024-03-25 14:54:59.561058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8fd2d76e554'
down_revision: Union[str, None] = '4dbb859374bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.execute("""
        INSERT INTO clients (name, lastname, account_id, email, phone, is_deleted)
        VALUES
            ('Marlon', 'Martinez', '6600c7733cbe0eafbed475c8', 'martinez.ded@gmail.com', '6182751570', false),
            ('Marlon1', 'Martinez', '6600c7733cbe0eafbed475c8', 'martinez.1ded@gmail.com', '6182751570', false),
            ('Marlon2', 'Martinez', '6600c7733cbe0eafbed475c8', 'martinez.2ded@gmail.com', '6182751570', false)
    """)

def downgrade():
    pass  # No action needed for downgrade
