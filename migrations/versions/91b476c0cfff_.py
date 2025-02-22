"""empty message

Revision ID: 91b476c0cfff
Revises: 991e3867ce55
Create Date: 2022-12-09 02:14:09.603073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91b476c0cfff'
down_revision = '991e3867ce55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=20), nullable=False),
    sa.Column('diameter', sa.String(length=28), nullable=False),
    sa.Column('gravity', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('diameter')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
