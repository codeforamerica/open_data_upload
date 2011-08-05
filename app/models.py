"""Models for the Open Data Boston upload form."""

from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dataset(db.Model):
    """Model for uploaded datasets."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String(150))
    phone = db.Column(db.String)
    file_name = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String)
    description = db.Column(db.Text)

    def __init__(self, **kwargs):
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])

    def __repr__(self):
        return '< %s >' % self.title
