from flask import Flask, jsonify
from flask_migrate import Migrate
from marshmallow import ValidationError

from flaskapp.settings import ENVIRONMENT, DATABASE_URL
from flaskapp.db import db


class App:
    def set_up(self):
        app = Flask(__name__)
        app.config.update(
            ENV=ENVIRONMENT,
            DEBUG=ENVIRONMENT == 'development',
            SQLALCHEMY_DATABASE_URI=DATABASE_URL,
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

        self.__set_up_database(app)
        self.__register_error_handlers(app)

        return app

    def __set_up_database(self, app):
        db.init_app(app)
        Migrate(app, db)

    def __register_error_handlers(self, app):
        @app.errorhandler(ValidationError)
        def request_validation_error(e):
            code = 'INPUT_VALIDATION_ERROR'
            details = []

            for field, errors in e.messages.items():
                details.append({
                    'target': field,
                    'errors': errors
                })

            return jsonify(code=code, message='Some fields are not valid', details=details), 400


app = App().set_up()
