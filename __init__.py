from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from background_tasks.sensors_handler import SensorHandler


db = SQLAlchemy()
sensors_handler = SensorHandler()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key = os.urandom(25)

    db.init_app(app)
    sensors_handler.start()

    with app.app_context():
        db.create_all()

        from routes import content, errors

        app.register_blueprint(content.content_)
        app.register_blueprint(errors.errors_)

        return app
