"""empty message

Revision ID: e2ac4e9538ae
Revises: 69049db2b6f7
Create Date: 2021-03-06 12:00:24.378536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2ac4e9538ae'
down_revision = '69049db2b6f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item_buy', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item_buy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###