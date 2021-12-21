"""modified date to datetime

Revision ID: a5ee169d9449
Revises: 
Create Date: 2021-12-21 17:24:59.338610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ee169d9449'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('barber',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('name', sa.String(length=50), nullable=False),
	sa.Column('document', sa.String(length=20), nullable=False, unique=True),
	sa.Column('phone', sa.String(length=20), nullable=True),
	sa.Column('create_at', sa.DateTime(), default=sa.func.now()),
	sa.Column('update_at', sa.DateTime(), default=sa.func.now()),
	sa.PrimaryKeyConstraint('id')
	)


def downgrade():
  op.drop_table('barber')
