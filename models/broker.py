from datetime import datetime

from models.agency import Agency
from utils.extensions import db
from sqlalchemy.sql import func


class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    created_time = db.Column(db.DateTime(timezone=True), default=func.now())
    modified_at = db.Column(db.DateTime(timezone=True), default=func.now())
    deleted = db.Column(db.Boolean, default=False)
    agency_id = db.Column(db.Integer, db.ForeignKey(Agency.id), nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)

    def __init__(self, agency_id, first_name, last_name, email, address):
        self.agency_id = agency_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.created_time = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return '<BrokerModel %r>' % self.email
