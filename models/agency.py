from datetime import datetime

from sqlalchemy import func

from utils.extensions import db


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    created_time = db.Column(db.DateTime(timezone=True), default=func.now())
    modified_at = db.Column(db.DateTime(timezone=True), default=func.now())
    deleted = db.Column(db.Boolean, default=False)
    domain = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __init__(self, domain, title, address):
        self.title = title
        self.domain = domain
        self.address = address
        self.created_time = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return '<AgencyModel %r>' % self.domain


