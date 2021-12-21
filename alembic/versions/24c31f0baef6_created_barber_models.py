"""created barber models

Revision ID: 24c31f0baef6
Revises: 
Create Date: 2021-12-21 14:13:41.267399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c31f0baef6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('barber',
	sa.Column('id', sa.Integer(), autoincrement=True),
	sa.Column('name', sa.String(length=250), nullable=False),
	sa.Column('document', sa.String(length=20), nullable=False),
	sa.Column('phone', sa.String(length=20), nullable=True),
	sa.Column('create_at', sa.TIMESTAMP()),
	sa.Column('update_at', sa.TIMESTAMP()),
	sa.PrimaryKeyConstraint('id')
	)


def downgrade():
	op.drop_table('barber')
