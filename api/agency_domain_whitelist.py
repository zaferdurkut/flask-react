from flask import jsonify, Blueprint, request

from manager.agency import AgencyManager
from manager.white_list import AgencyDomainWhitelistManager
from models.agency import Agency
from models.agency_domain_whitelist import AgencyDomainWhitelist
from schemas.agency import agency_output_schema, agency_list_output_schema, agency_input_schema
from schemas.agency_domain_whitelist import agency_domain_whitelist_list_schema, agency_domain_whitelist_schema, \
    agency_domain_whitelist_input_schema

from marshmallow.exceptions import ValidationError

blueprint_agencies_domain_whitelist = Blueprint("/api/agencies-domain-whitelist",
                                                __name__,
                                                url_prefix="/api/agencies-domain-whitelist")


class AgencyDomainWhitelistController(object):

    @staticmethod
    @blueprint_agencies_domain_whitelist.route("/", methods=["GET"])
    def get_all_agency():
        manager = AgencyDomainWhitelistManager()
        items = manager.get_all_agency_domain_whitelist()
        result = agency_domain_whitelist_list_schema.dump(items)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_agencies_domain_whitelist.route("/<int:id>", methods=["GET"])
    def get_agency(id):
        manager = AgencyDomainWhitelistManager()
        item = manager.get_agency_domain_whitelist_by_id(id)
        result = agency_domain_whitelist_schema.dump(item)
        return jsonify(result.data), 200

    @staticmethod
    @blueprint_agencies_domain_whitelist.route("/", methods=["POST"])
    def add_agency():
        manager = AgencyDomainWhitelistManager()
        try:
            schmea_item = agency_domain_whitelist_input_schema.load(request.json).data
            item = manager.add_item(AgencyDomainWhitelist(**schmea_item))
            result = agency_domain_whitelist_schema.dump(item)
            return jsonify(result.data), 200
        except ValidationError as exc:
            return jsonify({"info": str(exc)}), 400

    @staticmethod
    @blueprint_agencies_domain_whitelist.route("/<int:id>", methods=["DELETE"])
    def delete_agency(id):
        manager = AgencyDomainWhitelistManager()
        item = manager.get_agency_domain_whitelist_by_id(id)
        if item is not None:
            result = manager.db_delete(item)
            return jsonify(item.id), 200
        else:
            return jsonify({"info": "Agency not found"}), 404
