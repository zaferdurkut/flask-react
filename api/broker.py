from flask import jsonify, Blueprint, request
from marshmallow.exceptions import ValidationError

from manager.broker import BrokerManager
from models.agency import Agency
from models.broker import Broker
from schemas.agency import agency_output_schema, agency_input_schema
from schemas.broker import broker_output_list_schema, broker_output_schema, broker_input_schema
from service.broker_service import BrokerService
from sqlalchemy.exc import IntegrityError



blueprint_brokers = Blueprint("/api/brokers", __name__, url_prefix="/api/brokers")


class BrokerController(object):

    @staticmethod
    @blueprint_brokers.route("/", methods=["GET"])
    def get_all_broker():
        manager = BrokerManager()
        items = manager.get_all_brokers()
        result = broker_output_list_schema.dump(items)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_brokers.route("/<int:id>", methods=["GET"])
    def get_broker(id):
        manager = BrokerManager()
        item = manager.get_broker_by_id(id)
        result = broker_output_schema.dump(item)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_brokers.route("/", methods=["POST"])
    def add_broker():
        try:
            print(request.json)
            manager = BrokerManager()
            schmea_item = broker_input_schema.load(request.json).data

            schmea_item = BrokerService().find_agency_id(schmea_item)

            if schmea_item is False:
                return jsonify({"info": "Your email domain does not match the our agencies"}), 412

            item = manager.add_item(Broker(**schmea_item))
            result = broker_output_schema.dump(item)
            return jsonify(result.data), 200
        except ValidationError as exc:
            return jsonify({"info": str(exc)}), 400
        except IntegrityError as exc:
            return jsonify({"info": "Your record already exists"}), 400
        except Exception as exc:
            return jsonify({"info": str(exc)}), 422

    @staticmethod
    @blueprint_brokers.route("/<int:id>", methods=["DELETE"])
    def delete_broker(id):
        manager = BrokerManager()
        item = manager.get_broker_by_id(id)
        if item is not None:
            result = manager.db_delete(item)
            return jsonify(item.id), 200
        else:
            return jsonify({"info": "Agency not found"}), 404
