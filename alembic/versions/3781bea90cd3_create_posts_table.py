"""create posts table

Revision ID: 3781bea90cd3
Revises:
Create Date: 2023-05-31 13:28:48.898473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3781bea90cd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
