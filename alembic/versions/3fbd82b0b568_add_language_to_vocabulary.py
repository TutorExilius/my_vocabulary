"""add_language_to_vocabulary

Revision ID: 3fbd82b0b568
Revises: f60a5910a5d2
Create Date: 2021-07-12 19:54:15.769070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbd82b0b568'
down_revision = 'f60a5910a5d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vocabulary', sa.Column('language', sa.Enum('ENGLISH', 'FRENCH', 'GERMAN', name='language'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vocabulary', 'language')
    # ### end Alembic commands ###