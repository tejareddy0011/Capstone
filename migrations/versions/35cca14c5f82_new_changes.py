"""new changes

Revision ID: 35cca14c5f82
Revises: 
Create Date: 2024-11-29 16:36:21.972725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35cca14c5f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('experience', sa.String(length=255), nullable=True),
    sa.Column('skills', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_jobs_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('cv_filename', sa.String(length=256), nullable=False),
    sa.Column('applied_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name='fk_applications_job_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_applications_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applications')
    op.drop_table('jobs')
    op.drop_table('users')
    # ### end Alembic commands ###
