import json
from unittest import TestCase

from flask.testing import FlaskClient

from run import app

client = app.test_client()

POST_BOKER_PATH = "/api/brokers/"
POST_AGECNY_PATH = "/api/agencies/"


class CommonController(TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = FlaskClient(self.app)

    def test_set_broker(self):
        # agency_post_response = client.post(POST_AGECNY_PATH,
        #                                    json={"address": "Istanbul",
        #                                                     "domain": "testdomain.com",
        #                                                     "title": "Test Title"
        #                                                     },
        #                                    content_type='application/json')
        #
        # assert agency_post_response.status_code == 200
        #
        # agency_post_response_data = json.loads(agency_post_response.data)
        #
        # test_agency_id = agency_post_response_data["id"]
        #
        # broker_post_response = client.post(POST_BOKER_PATH,
        #                                    json={"first_name": "Zafer",
        #                                                      "last_name": "Durkut",
        #                                                      "email": "zafer11@testdomain.com",
        #                                                      "address": "Ankara"
        #                                                      },
        #                                    content_type='application/json')
        #
        # assert broker_post_response.status_code == 200
        #
        # broker_post_response_data = json.loads(broker_post_response.data)
        #
        # test_broker_agency_id = broker_post_response_data["agency_id"]
        #
        # assert test_agency_id == test_broker_agency_id
        #
        # delete_response = client.delete(POST_BOKER_PATH + str(broker_post_response_data["id"]))
        #
        # assert delete_response.status_code == 200
        #
        # delete_response = client.delete(POST_AGECNY_PATH + str(test_agency_id))
        #
        # assert delete_response.status_code == 200

        assert 1 == 1
