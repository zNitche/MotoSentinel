from flask import Blueprint, jsonify, current_app
from app_config import AppConfig


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route(f"/api/sensors/<sensor_name>")
def sensor_data(sensor_name):
    sensors_manager = current_app.config[AppConfig.SENSORS_MANAGER_CONFIG_KEY_NAME]

    data = sensors_manager.get_sensor_parsed_data_by_sensor_name(sensor_name)

    return jsonify(data)
