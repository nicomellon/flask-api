"""Create the User table

Revision ID: 524fcdf1548e
Revises: 
Create Date: 2023-01-26 19:50:26.153218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '524fcdf1548e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=64), nullable=True),
                    sa.Column('email', sa.String(length=120), nullable=True),
                    sa.Column('password_hash', sa.String(length=128), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
