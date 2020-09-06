from flask import jsonify, Blueprint, request

from manager.agency import AgencyManager
from models.agency import Agency
from schemas.agency import agency_output_schema, agency_list_output_schema, AgencyInputSchema, agency_input_schema
from marshmallow.exceptions import ValidationError


blueprint_agencies = Blueprint("/api/agencies", __name__, url_prefix="/api/agencies")


class AgencyController(object):

    @staticmethod
    @blueprint_agencies.route("/", methods=["GET"])
    def get_all_agency():
        manager = AgencyManager()
        items = manager.get_all_agencies()
        result = agency_list_output_schema.dump(items)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_agencies.route("/<int:id>", methods=["GET"])
    def get_agency(id):
        manager = AgencyManager()
        item = manager.get_agency_by_id(id)
        result = agency_output_schema.dump(item)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_agencies.route("/", methods=["POST"])
    def add_agency():
        try:
            manager = AgencyManager()
            schmea_item = agency_input_schema.load(request.json).data
            item = manager.add_item(Agency(**schmea_item))
            result = agency_output_schema.dump(item)
            return jsonify(result.data), 200
        except ValidationError as exc:
            return jsonify({"info": str(exc)}), 400

    @staticmethod
    @blueprint_agencies.route("/<int:id>", methods=["DELETE"])
    def delete_agency(id):
        manager = AgencyManager()
        item = manager.get_agency_by_id(id)
        if item is not None:
            result = manager.db_delete(item)
            return jsonify(item.id), 200
        else:
            return jsonify({"info": "Agency not found"}), 404
