from flask import redirect, Blueprint, url_for, request
from utils import settings_utils
from app_config import AppConfig


settings_ = Blueprint("settings", __name__, template_folder='template', static_folder='static')


@settings_.route("/settings/graphs/set_time_range", methods=["GET"])
def set_time_range():
    if request.args.get("time_range"):
        refresh_rate = int(request.args.get("time_range"))

        settings_data = settings_utils.load_settings()

        settings_data[AppConfig.SETTINGS_TIME_RANGE_KEY_NAME] = refresh_rate

        settings_utils.save_settings(settings_data)

    return redirect(url_for("content.settings"))
