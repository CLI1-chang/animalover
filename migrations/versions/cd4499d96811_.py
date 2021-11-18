"""empty message

Revision ID: cd4499d96811
Revises: d4af25262fdd
Create Date: 2021-11-17 21:22:49.998436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4499d96811'
down_revision = 'd4af25262fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('association', schema=None) as batch_op:
        batch_op.alter_column('animal_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('association', schema=None) as batch_op:
        batch_op.alter_column('animal_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###