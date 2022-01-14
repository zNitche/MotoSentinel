from flask import Blueprint, jsonify, current_app
from app_config import AppConfig


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route("/api/sensors/<sensor_name>")
def sensor_data(sensor_name):
    sensors_manager = current_app.config[AppConfig.SENSORS_MANAGER_CONFIG_KEY_NAME]

    data = sensors_manager.get_sensor_parsed_data_by_sensor_name(sensor_name)

    return jsonify(data)


@sensors_.route("/api/sensors")
def sensors_list():
    sensors_manager = current_app.config[AppConfig.SENSORS_MANAGER_CONFIG_KEY_NAME]

    sensors = [sensor.name for sensor in sensors_manager.get_sensors()]

    return jsonify(sensors)
