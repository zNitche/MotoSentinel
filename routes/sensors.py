from flask import Blueprint, jsonify


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route("/sensors/gyro")
def gyro():
    from app import sensors_manager

    return jsonify(sensors_manager.get_gyro_parsed_data())


@sensors_.route("/sensors/accelerometer")
def accelerometer():
    from app import sensors_manager

    return jsonify(sensors_manager.get_accelerometer_parsed_data())
