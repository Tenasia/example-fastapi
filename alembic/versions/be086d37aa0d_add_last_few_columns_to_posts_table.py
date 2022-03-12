"""add last few columns to posts table

Revision ID: be086d37aa0d
Revises: d4170bd88464
Create Date: 2022-03-12 12:45:52.053472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be086d37aa0d'
down_revision = 'd4170bd88464'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    pass
