"""add foreign key to post table

Revision ID: d4170bd88464
Revises: 0ef6a30e0ec5
Create Date: 2022-03-12 12:36:27.745876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4170bd88464'
down_revision = '0ef6a30e0ec5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
    sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
