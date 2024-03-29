"""Initial Migration

Revision ID: b702e7dd7ded
Revises: 
Create Date: 2023-05-02 17:13:36.877926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b702e7dd7ded"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "portfolio_project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("description", sa.String(length=1024), nullable=False),
        sa.Column("website_link", sa.String(length=128), nullable=False),
        sa.Column("body", sa.String(length=2048), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("portfolio_project")
    # ### end Alembic commands ###
