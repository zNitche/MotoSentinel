from flask import redirect, Blueprint, url_for, request
from utils import settings_utils


settings_ = Blueprint("settings", __name__, template_folder='template', static_folder='static')


@settings_.route("/settings/graphs/set_time_range/<mode>/", methods=["GET"])
def set_time_range(mode):
    if request.args.get(mode):
        refresh_rate = int(request.args.get(mode))

        settings_data = settings_utils.load_settings()

        settings_data[mode] = refresh_rate

        settings_utils.save_settings(settings_data)

    return redirect(url_for("content.settings"))
