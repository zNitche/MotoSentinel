from flask import Blueprint, jsonify, current_app
from app_config import AppConfig
from utils import db_utils
from sensors.sensors_config import SensorsConfig

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


@sensors_.route("/api/sensors_data/<sensor_name>")
def sensors_db_data(sensor_name):
    sensor_db_data = []

    if sensor_name == SensorsConfig.ACCELEROMETER_SENSOR_NAME:
        sensor_db_data = db_utils.get_acceleration_data()

    elif sensor_name == SensorsConfig.GYRO_SENSOR_NAME:
        sensor_db_data = db_utils.get_gyro_data()

    elif sensor_name == SensorsConfig.TEMP_SENSOR_NAME:
        sensor_db_data = db_utils.get_temp_data()

    return jsonify(sensor_db_data)
