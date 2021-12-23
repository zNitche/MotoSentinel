from __init__ import create_app, db
from background_tasks.sensors_handler import SensorHandler
from background_tasks.db_handler import DBHandler


app = create_app()

sensors_handler = SensorHandler()
db_handler = DBHandler(app, db, sensors_handler)

sensors_handler.start()
db_handler.start()

if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)
