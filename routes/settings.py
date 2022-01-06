from flask import redirect, Blueprint, url_for, request
from utils import settings_utils
from settings_config import SettingsConfig

settings_ = Blueprint("settings", __name__, template_folder='template', static_folder='static')


@settings_.route("/settings/apply_settings", methods=["POST"])
def apply_settings():
    requests_dict = request.form.to_dict()

    if len(requests_dict.keys()) > 0:
        settings_data = settings_utils.load_settings()

        for settings_mode in requests_dict:
            if settings_mode in settings_data.keys():
                settings_mode_value = requests_dict[settings_mode]

                if settings_mode_value:
                    if settings_mode_value.isnumeric():
                        settings_mode_value = int(settings_mode_value)

                    settings_data[settings_mode] = settings_mode_value

        settings_utils.save_settings(settings_data)

    return redirect(url_for("content.settings"))
