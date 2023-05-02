import sqlalchemy as sa

from ferialabs import db


class Project(db.Base):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(512), unique=True, nullable=False)
    description = sa.Column(sa.String(1024), nullable=False)
    website_link = sa.Column(sa.String(128), nullable=False)
    body = sa.Column(sa.String(2048), nullable=False)

    __tablename__ = "portfolio_project"

    def __repr__(self):
        return self.title
