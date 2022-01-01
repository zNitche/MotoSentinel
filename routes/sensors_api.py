from flask import Blueprint, jsonify, current_app


sensors_ = Blueprint("sensors", __name__, template_folder='template', static_folder='static')


@sensors_.route(f"/sensors/<sensor_name>")
def sensor_data(sensor_name):
    sensors_manager = current_app.config["SENSORS_MANAGER"]

    data = sensors_manager.get_sensor_parsed_data_by_sensor_name(sensor_name)

    return jsonify(data)
