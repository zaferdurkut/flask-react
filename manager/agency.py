from models.agency import Agency
from models.agency_domain_whitelist import AgencyDomainWhitelist

from utils.extensions import db


class AgencyManager(object):

    def __init__(self):
        self.db = db

    def get_agency_by_id(self, id: int) -> Agency:
        return Agency.query.filter(Agency.id == id, Agency.deleted == False).first()

    def get_matching_agency_by_domain(self, domain: str, retry: bool = False):

        is_exist_domain = AgencyDomainWhitelist.query.filter(Agency.domain == domain, Agency.deleted == False).count()

        if is_exist_domain < 1:
            return False

        item_count = Agency.query.filter(Agency.domain == domain, Agency.deleted == False).count()

        if item_count < 1:
            return False

        elif item_count == 1:
            return Agency.query.filter(Agency.domain == domain, Agency.deleted == False).first()

        elif item_count > 1 and retry is True:
            item = Agency.query.filter(Agency.domain == domain, Agency.deleted == False).order_by(Agency.created_time.asc()).first()

            return item

        else:
            return None

    def get_agency_by_domain(self, domain: str):

        return Agency.query.filter(Agency.domain == domain, Agency.deleted == False).all()

    def get_all_agencies(self):
        return Agency.query.filter(Agency.deleted == False).all()

    def add_item(self, agency: Agency):
        domain_item = AgencyDomainWhitelist(domain=agency.domain)

        self.db.session.add(domain_item)
        self.db.session.add(agency)
        self.db.session.commit()
        return agency

    def db_delete(self, agency: Agency):
        # self.db.session.delete(agency)
        agency.deleted = True
        self.db.session.commit()
        return agency
