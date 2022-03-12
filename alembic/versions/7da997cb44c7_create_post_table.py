"""create post table

Revision ID: 7da997cb44c7
Revises: 
Create Date: 2022-03-12 12:13:08.802086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da997cb44c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts',)
    pass
