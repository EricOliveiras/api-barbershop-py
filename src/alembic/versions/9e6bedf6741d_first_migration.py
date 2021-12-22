"""first migration

Revision ID: 9e6bedf6741d
Revises: 
Create Date: 2021-12-22 11:16:49.397107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e6bedf6741d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
		'barber',
		sa.Column('id', sa.Integer(), autoincrement=True),
		sa.Column('name', sa.String(length=100), nullable=False),
		sa.Column('document', sa.String(length=20), nullable=False, unique=True),
		sa.Column('phone', sa.String(length=20), nullable=True),
		sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
		sa.Column('updated_at', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now()),
		sa.PrimaryKeyConstraint('id')
	)


def downgrade():
  op.drop_table('barber')
