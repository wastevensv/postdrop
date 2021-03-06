"""Added user-notes relationship.

Revision ID: bb185ea22eff
Revises: e7428295c684
Create Date: 2016-06-08 21:55:39.604973

"""

# revision identifiers, used by Alembic.
revision = 'bb185ea22eff'
down_revision = 'e7428295c684'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('owner', 'users', ['owner_id'], ['id'])

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.drop_constraint('owner', type_='foreignkey')
        batch_op.drop_column('owner_id')

    ### end Alembic commands ###
