import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DO_LOGS = True
    LOGS_PATH = os.path.join(CURRENT_DIR, "log.txt")

    SETTINGS_PATH = os.path.join(CURRENT_DIR, "settings.json")

    PNG_ENCODE_STRING = "data:image/png;base64,"
    GRAPH_DPI_RESOLUTION = 150

    SETTINGS_TIME_RANGE_KEY_NAME = "time_range"
    DEFAULT_TIME_RANGE = 60
