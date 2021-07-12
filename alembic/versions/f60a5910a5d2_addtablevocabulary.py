"""addTableVocabulary

Revision ID: f60a5910a5d2
Revises: 
Create Date: 2021-07-12 19:32:33.718529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f60a5910a5d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vocabulary',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('word', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vocabulary')
    # ### end Alembic commands ###