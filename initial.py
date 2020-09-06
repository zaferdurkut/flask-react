import csv

from models.agency import Agency
from models.agency_domain_whitelist import AgencyDomainWhitelist
from models.broker import Broker
from utils.extensions import db


def agency_intial_data():
    if len(Agency.query.filter().all()) == 0:
        with open('resources/agency.csv', 'r') as csv_file:
            csv_records = csv.reader(csv_file, delimiter=',')
            next(csv_records)
            for row in csv_records:
                item = Agency(title=row[1], domain=row[2], address=row[3])
                db.session.add(item)
                db.session.commit()
                print("inserted", item)
    return True

def agency_domain_whitelist_inital_data():
    if len(AgencyDomainWhitelist.query.filter().all()) == 0:
        with open('resources/agency_domain_whitelist.csv', 'r') as csv_file:
            csv_records = csv.reader(csv_file, delimiter=',')
            next(csv_records)
            for row in csv_records:
                item = AgencyDomainWhitelist(domain=row[1],)
                db.session.add(item)
                db.session.commit()
                print("inserted", item)
    return True


def run_insert_job():
    agency_data_status = agency_intial_data()
    agency_domain_whitelist_status = agency_domain_whitelist_inital_data()

    return agency_data_status, agency_domain_whitelist_status

if __name__ == "__main__":
    run_insert_job()
