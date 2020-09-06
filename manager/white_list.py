from models.agency_domain_whitelist import AgencyDomainWhitelist

from utils.extensions import db


class AgencyDomainWhitelistManager(object):

    def __init__(self):
        self.db = db

    def get_agency_domain_whitelist_by_id(self, id: int) -> AgencyDomainWhitelist:
        return AgencyDomainWhitelist.query.filter(AgencyDomainWhitelist.id == id,
                                                  AgencyDomainWhitelist.deleted == False).first()

    def get_all_agency_domain_whitelist(self):
        return AgencyDomainWhitelist.query.filter(AgencyDomainWhitelist.deleted == False).all()

    def add_item(self, agency_domain_whitelist: AgencyDomainWhitelist):
        self.db.session.add(agency_domain_whitelist)
        self.db.session.commit()
        return agency_domain_whitelist

    def db_delete(self, agency_domain_whitelist: AgencyDomainWhitelist):
        # self.db.session.delete(agency_domain_whitelist)
        agency_domain_whitelist.deleted = True
        self.db.session.commit()
        return agency_domain_whitelist
