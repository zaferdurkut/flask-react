from flask import request, jsonify, Blueprint

from initial import run_insert_job

blueprint_common = Blueprint("/api/common", __name__, url_prefix="/api/common")


@blueprint_common.route("/", methods=["GET"])
def status():
    return jsonify({"status": True})


@blueprint_common.route("/inital-data", methods=["GET"])
def inital_data():
    agency_data_status, agency_domain_whitelist_status = run_insert_job()
    return jsonify({"agency_insert_data_status": agency_data_status,
                    "agency_domain_whitelist_insert_data_status": agency_domain_whitelist_status})
