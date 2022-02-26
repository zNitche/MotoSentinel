import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False

    SENSORS_MANAGER_CONFIG_KEY_NAME = "SENSORS_MANAGER"
    DB_MANAGER_CONFIG_KEY_NAME = "DB_MANAGER"

    DATA_PATH = "data"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATA_PATH}/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DO_LOGS = True
    LOGS_PATH = os.path.join(CURRENT_DIR, DATA_PATH, "log.txt")

    SETTINGS_PATH = os.path.join(CURRENT_DIR, DATA_PATH, "settings.json")

    PNG_ENCODE_STRING = "data:image/png;base64,"
    GRAPH_DPI_RESOLUTION = 150
