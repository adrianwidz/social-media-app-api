"""add content column to posts table

Revision ID: d6ec455b734e
Revises: 3781bea90cd3
Create Date: 2023-06-01 04:55:53.168867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6ec455b734e'
down_revision = '3781bea90cd3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
