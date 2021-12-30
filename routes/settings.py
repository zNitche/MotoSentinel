from flask import redirect, Blueprint, url_for, request
from utils import settings_utils
from app_config import AppConfig


settings_ = Blueprint("settings", __name__, template_folder='template', static_folder='static')


@settings_.route("/settings/graphs/set_refresh", methods=["GET"])
def graphs_set_refresh():
    if request.args.get("refresh_rate"):
        refresh_rate = int(request.args.get("refresh_rate"))

        settings_data = settings_utils.load_settings()

        settings_data[AppConfig.SETTINGS_REFRESH_RATE_KEY_NAME] = refresh_rate

        settings_utils.save_settings(settings_data)

    return redirect(url_for("content.settings"))
