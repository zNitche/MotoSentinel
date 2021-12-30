import json
import os
from app_config import AppConfig


def init_settings():
    if not os.path.exists(AppConfig.SETTINGS_PATH):
        settings_data = {
            AppConfig.SETTINGS_TIME_RANGE_KEY_NAME: AppConfig.DEFAULT_TIME_RANGE
        }

        with open(AppConfig.SETTINGS_PATH, "w") as settings_file:
            settings_file.write(json.dumps(settings_data, indent=4))


def load_settings():
    with open(AppConfig.SETTINGS_PATH, "r") as settings_file:
        settings_data = json.loads(settings_file.read())

    return settings_data


def save_settings(settings_data):
    with open(AppConfig.SETTINGS_PATH, "w") as settings_file:
        settings_file.write(json.dumps(settings_data, indent=4))
