from flask import redirect, Blueprint, url_for, request
from utils import settings_utils


settings_ = Blueprint("settings", __name__, template_folder='template', static_folder='static')


@settings_.route("/settings/apply_settings", methods=["GET"])
def apply_settings():
    requests_dict = request.args.to_dict()

    if len(requests_dict.keys()) > 0:
        for settings_mode in requests_dict:
            settings_data = settings_utils.load_settings()

            settings_mode_value = requests_dict[settings_mode]

            if settings_mode_value.isnumeric():
                settings_mode_value = int(settings_mode_value)

            settings_data[settings_mode] = settings_mode_value

            settings_utils.save_settings(settings_data)

    return redirect(url_for("content.settings"))
