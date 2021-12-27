import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DO_LOGS = True
    LOGS_PATH = os.path.join(CURRENT_DIR, "log.txt")
