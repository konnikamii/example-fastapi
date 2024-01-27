"""create posts table

Revision ID: 010aebc82946
Revises: 
Create Date: 2024-01-20 10:57:48.832280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '010aebc82946'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key= True), 
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content',sa.String(),nullable=False),
                    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,server_default= sa.text('NOW()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
