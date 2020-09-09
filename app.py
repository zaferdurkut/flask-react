import os
from flask import Flask, make_response
from flask_migrate import Migrate
from dotenv import load_dotenv

from api.agency import blueprint_agencies
from api.agency_domain_whitelist import blueprint_agencies_domain_whitelists
from api.broker import blueprint_brokers
from api.common import blueprint_common
from config.config import config
from utils.extensions import db
from flask_cors import CORS


load_dotenv()
ENV = os.getenv('ENV', 'default')

if ENV not in config:
    raise Exception('Invalid ENV: %s' % ENV)


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(config[ENV]())
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register extensions."""
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register blueprints."""
    app.register_blueprint(blueprint_common)
    app.register_blueprint(blueprint_agencies)
    app.register_blueprint(blueprint_agencies_domain_whitelists)
    app.register_blueprint(blueprint_brokers)

    return None
