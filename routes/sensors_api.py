from flask import Blueprint, jsonify


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route(f"/sensors/<sensor_name>")
def sensor_data(sensor_name):
    from app import sensors_manager

    data = sensors_manager.get_sensor_parsed_data_by_sensor_name(sensor_name)

    return jsonify(data)
