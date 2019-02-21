"""修改user表

Revision ID: 448357ee9e9e
Revises: 519889eafce2
Create Date: 2019-02-21 15:33:21.740000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '448357ee9e9e'
down_revision = '519889eafce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
