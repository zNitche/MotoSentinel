from flask import Blueprint, jsonify, current_app
from utils import db_utils
from sensors.sensors_config import SensorsConfig

sensors = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors.route("/api/sensors/<sensor_name>")
def sensor_data(sensor_name):
    sensors_manager = current_app.sensors_manager

    data = sensors_manager.get_sensor_parsed_data_by_sensor_name(sensor_name)

    return jsonify(data)


@sensors.route("/api/sensors")
def sensors_list():
    sensors_manager = current_app.sensors_manager

    sensors = [sensor.name for sensor in sensors_manager.get_sensors()]

    return jsonify(sensors)


@sensors.route("/api/sensors_data/<sensor_name>")
def sensors_db_data(sensor_name):
    sensor_db_data = []

    if sensor_name == SensorsConfig.ACCELEROMETER_SENSOR_NAME:
        sensor_db_data = db_utils.get_acceleration_data()

    elif sensor_name == SensorsConfig.GYRO_SENSOR_NAME:
        sensor_db_data = db_utils.get_gyro_data()

    elif sensor_name == SensorsConfig.TEMP_SENSOR_NAME:
        sensor_db_data = db_utils.get_temp_data()

    return jsonify(sensor_db_data)
