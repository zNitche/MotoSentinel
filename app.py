from __init__ import create_app
from utils import settings_utils


app = create_app()

if __name__ == "__main__":
    settings_utils.init_settings()

    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT)
