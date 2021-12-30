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


class SettingsConfig:
    SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME = "acceleration_time_range"
    DEFAULT_ACCELERATION_TIME_RANGE = 60

    SETTINGS_STRUCT = {
        SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME: DEFAULT_ACCELERATION_TIME_RANGE
    }
