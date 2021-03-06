"""create new migrations

Revision ID: 301a1934b703
Revises: 
Create Date: 2022-01-08 11:15:06.562305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301a1934b703'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barber',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('document', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime()),
    sa.Column('updated_at', sa.DateTime(), onupdate=sa.func.now()),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('document')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime()),
    sa.Column('updated_at', sa.DateTime(), onupdate=sa.func.now()),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('barber_id', sa.Integer(), nullable=False),
    sa.Column('total_payment', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime()),
    sa.Column('updated_at', sa.DateTime(), onupdate=sa.func.now()),
    sa.ForeignKeyConstraint(['barber_id'], ['barber.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('barber_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime()),
    sa.Column('updated_at', sa.DateTime(), onupdate=sa.func.now()),
    sa.ForeignKeyConstraint(['barber_id'], ['barber.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('payment')
    op.drop_table('client')
    op.drop_table('barber')
    # ### end Alembic commands ###
