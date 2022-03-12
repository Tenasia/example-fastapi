"""addd content column

Revision ID: b98310977d6f
Revises: 7da997cb44c7
Create Date: 2022-03-12 12:23:47.506866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b98310977d6f'
down_revision = '7da997cb44c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
