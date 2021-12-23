from __init__ import create_app, db
from background_managers.sensors_manager import SensorManager
from background_managers.db_manager import DBManager


app = create_app()

sensors_manager = SensorManager()
db_manager = DBManager(app, db, sensors_manager)

sensors_manager.start()
db_manager.start()

if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)
