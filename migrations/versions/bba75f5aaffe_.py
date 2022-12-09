"""empty message

Revision ID: bba75f5aaffe
Revises: 91b476c0cfff
Create Date: 2022-12-09 02:18:21.183721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba75f5aaffe'
down_revision = '91b476c0cfff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('climate', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('diameter', sa.String(length=28), nullable=False))
        batch_op.add_column(sa.Column('gravity', sa.String(length=10), nullable=False))
        batch_op.create_unique_constraint(None, ['diameter'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('gravity')
        batch_op.drop_column('diameter')
        batch_op.drop_column('climate')

    # ### end Alembic commands ###
