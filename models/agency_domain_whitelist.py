from datetime import datetime
from utils.extensions import db
from sqlalchemy.sql import func


class AgencyDomainWhitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    created_time = db.Column(db.DateTime(timezone=True), default=func.now())
    modified_at = db.Column(db.DateTime(timezone=True), default=func.now())
    deleted = db.Column(db.Boolean, default=False)
    domain = db.Column(db.String, nullable=False)

    def __init__(self, domain):
        self.domain = domain
        self.created_time = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return '<AgencyDomainWhitelist %r>' % self.domain
