from models.agency import Agency

from utils.extensions import db


class AgencyManager(object):

    def __init__(self):
        self.db = db

    def get_agency_by_id(self, id: int) -> Agency:
        return Agency.query.filter(Agency.id == id, Agency.deleted == False).first()

    def get_all_agencies(self):
        return Agency.query.filter(Agency.deleted == False).all()

    def add_item(self, agency: Agency):
        self.db.session.add(agency)
        self.db.session.commit()
        return agency

    def db_delete(self, agency: Agency):
        # self.db.session.delete(agency)
        agency.deleted = True
        self.db.session.commit()
        return agency
