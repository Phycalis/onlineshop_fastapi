"""field file_id(str) to products added

Revision ID: 5b6d1522a601
Revises: f2a3ac28c74e
Create Date: 2024-07-18 13:06:05.952027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b6d1522a601'
down_revision: Union[str, None] = 'f2a3ac28c74e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('file_id', sa.String(), nullable=True))
    op.alter_column('products', 'image',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'image',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('products', 'file_id')
    # ### end Alembic commands ###
