from utils.extensions import db

from models.broker import Broker
from psycopg2 import errors


class BrokerManager(object):

    def __init__(self):
        self.db = db

    def get_broker_by_id(self, id: int) -> Broker:
        return Broker.query.filter(Broker.id == id, Broker.deleted == False).first()

    def get_all_brokers(self):
        return Broker.query.filter(Broker.deleted == False).all()

    def add_item(self, broker: Broker):
        self.db.session.add(broker)
        self.db.session.commit()
        return broker

    def db_delete(self, broker: Broker):
        # self.db.session.delete(broker)
        broker.deleted = True
        self.db.session.commit()
        return broker
