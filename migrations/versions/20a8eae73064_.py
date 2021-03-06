"""empty message

Revision ID: 20a8eae73064
Revises: 922673af3887
Create Date: 2022-06-03 00:07:25.715010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a8eae73064'
down_revision = '922673af3887'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venue', sa.Column('genres', sa.String(), nullable=True))
    op.add_column('venue', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'website_link')
    op.drop_column('venue', 'genres')
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'website_link')
    # ### end Alembic commands ###
