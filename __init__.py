from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app_config.AppConfig")
    app.secret_key = os.urandom(25)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from routes import content, errors, sensors

        app.register_blueprint(content.content_)
        app.register_blueprint(errors.errors_)
        app.register_blueprint(sensors.sensors_)

        return app
