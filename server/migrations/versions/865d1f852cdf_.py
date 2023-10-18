"""empty message

Revision ID: 865d1f852cdf
Revises: 47478da88e6b
Create Date: 2023-10-18 15:27:56.926088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '865d1f852cdf'
down_revision = '47478da88e6b'
branch_labels = None
depends_on = None


def upgrade():
     # Create a new column
    op.add_column('baked_goods', sa.Column('new_created_at', sa.DateTime, nullable=True))

    # Create an SQL expression for the update
    update_sql = text("UPDATE baked_goods SET new_created_at = datetime(created_at)")

    # Execute the SQL expression
    conn = op.get_bind()
    conn.execute(update_sql)

    # Drop the old column
    op.drop_column('baked_goods', 'created_at')

    # Rename the new column to 'created_at'
    op.alter_column('baked_goods', 'new_created_at', new_column_name='created_at', existing_type=sa.DateTime)


def downgrade():
    
    pass
