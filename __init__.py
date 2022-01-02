from flask import Flask
import os
from models import db


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app_config.AppConfig")
    app.secret_key = os.urandom(25)

    db.init_app(app)

    from background_managers.sensors_manager import SensorManager
    from background_managers.db_manager import DBManager

    sensors_manager = SensorManager()
    sensors_manager.start()

    with app.app_context():
        db.create_all()

        db_manager = DBManager(app, db, sensors_manager)
        db_manager.start()

        app.config["DB_MANAGER"] = db_manager
        app.config["SENSORS_MANAGER"] = sensors_manager

        from routes import content, errors, sensors_api, settings

        app.register_blueprint(content.content_)
        app.register_blueprint(errors.errors_)
        app.register_blueprint(sensors_api.sensors_)
        app.register_blueprint(settings.settings_)

        return app
