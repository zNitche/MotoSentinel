from flask import Blueprint, jsonify
from sensors.sensors_config import SensorsConfig


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route(f"/sensors/{SensorsConfig.GYRO_SENSOR_NAME}")
def gyro():
    from app import sensors_manager

    return jsonify(sensors_manager.get_sensor_parsed_data_by_sensor_name(SensorsConfig.GYRO_SENSOR_NAME))


@sensors_.route(f"/sensors/{SensorsConfig.ACCELEROMETER_SENSOR_NAME}")
def accelerometer():
    from app import sensors_manager

    return jsonify(sensors_manager.get_sensor_parsed_data_by_sensor_name(SensorsConfig.ACCELEROMETER_SENSOR_NAME))
