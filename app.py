from flask import Flask
from flask_migrate import Migrate
from models import db, setup_db


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    return app
