from config.config import HERE_GEOCODING_URL, HERE_GEOCODING_API_KEY
from manager.agency import AgencyManager
from schemas.broker import BrokerInputSchema
import requests

from geopy import distance as distance_func


class BrokerService(object):

    def __init__(self):
        self.here_url = HERE_GEOCODING_URL
        self.here_api_key = HERE_GEOCODING_API_KEY

    def find_agency_id(self, broker_input_schema: BrokerInputSchema):
        broker_input_schema["agency_id"] = None

        domain = self.email_to_domain(broker_input_schema["email"])

        manager = AgencyManager()

        result = manager.get_matching_agency_by_domain(domain)

        if result is False:
            return False

        elif result is None:
            geocoding_match_items = None
            agency_list = manager.get_agency_by_domain(domain)

            locations = {}
            for agency in agency_list:
                longitude, latitude = self.get_address_locations(agency.address)
                locations[agency.id] = (latitude, longitude)

            longitude, latitude = self.get_address_locations(broker_input_schema["address"])

            main_location = (latitude, longitude)

            near_location_id = self.get_id_from_calculate_distance(locations=locations, main_location=main_location)

            if near_location_id is not None:
                geocoding_match_items = True

            broker_input_schema["agency_id"] = near_location_id

            if geocoding_match_items is None:
                result = manager.get_matching_agency_by_domain(domain, retry=True)
                broker_input_schema["agency_id"] = result.id

            return broker_input_schema

        else:
            broker_input_schema["agency_id"] = result.id

            return broker_input_schema

        return None

    def email_to_domain(self, email: str) -> str:

        return email.strip().split("@")[1]

    def get_address_locations(self, address: str):

        params = {'apikey': self.here_api_key, 'q': address}

        r = requests.get(url=self.here_url, params=params)
        data = r.json()
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']

        return longitude, latitude

    def get_id_from_calculate_distance(self, locations, main_location):

        near_location_id = 0
        near_location_distance = None
        print("main_location", main_location)
        for key, value in locations.items():
            distance = distance_func.distance(value, main_location).km

            print(key, value, near_location_distance)

            if near_location_distance is None:
                near_location_distance = distance
                near_location_id = key

            if distance < near_location_distance:
                near_location_distance = distance
                near_location_id = key

        print(near_location_id)
        return near_location_id
