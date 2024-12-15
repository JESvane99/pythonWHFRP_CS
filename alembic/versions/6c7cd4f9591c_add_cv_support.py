"""add cv support

Revision ID: 6c7cd4f9591c
Revises: d834ca5f3c12
Create Date: 2024-12-15 08:41:30.077296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7cd4f9591c'
down_revision: Union[str, None] = 'd834ca5f3c12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('group', sa.String()))
    op.create_table('Cv',
    sa.Column('id', sa.Integer()),
    sa.Column('character_id', sa.Integer()),
    sa.Column('group', sa.String()),
    sa.Column('career', sa.String()),
    sa.Column('status', sa.Integer()),
    sa.Column('careerpath', sa.String()),
    sa.ForeignKeyConstraint(('character_id',), ['character.id']),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'group')
    op.drop_table('Cv')
    # ### end Alembic commands ###