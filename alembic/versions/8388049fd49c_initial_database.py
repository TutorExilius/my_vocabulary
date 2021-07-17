"""initial_database

Revision ID: 8388049fd49c
Revises: 
Create Date: 2021-07-18 17:07:00.919482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8388049fd49c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cardbox',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tray',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('poll_interval', sa.Integer(), nullable=False),
    sa.Column('cardbox_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cardbox_id'], ['cardbox.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flashcard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('image_file', sa.String(), nullable=True),
    sa.Column('last_poll_date', sa.DateTime(), nullable=True),
    sa.Column('count_right', sa.Integer(), nullable=False),
    sa.Column('count_wrong', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('adult_only', sa.Boolean(), nullable=True),
    sa.Column('tray_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tray_id'], ['tray.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flashcardpage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('flashcard_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['flashcard_id'], ['flashcard.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('language', sa.Enum('ENGLISH', 'FRENCH', 'GERMAN', name='language'), nullable=False),
    sa.Column('audio_file', sa.String(), nullable=True),
    sa.Column('is_definition', sa.Boolean(), nullable=True),
    sa.Column('flashcardpage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['flashcardpage_id'], ['flashcardpage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('entry')
    op.drop_table('flashcardpage')
    op.drop_table('flashcard')
    op.drop_table('tray')
    op.drop_table('cardbox')
    # ### end Alembic commands ###
