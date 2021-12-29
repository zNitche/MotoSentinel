from flask import render_template, Blueprint
from sensors.sensors_config import SensorsConfig
from utils import graphs_utils


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    from app import sensors_manager

    sensors_data = [sensor.parse_sensors_data() for sensor in sensors_manager.get_sensors()]

    return render_template("index.html", sensors_data=sensors_data, sensors_config=SensorsConfig)


@content_.route("/settings")
def settings():
    return "Settings"


@content_.route("/graphs")
def graphs():
    sensors_graphs = [graphs_utils.generate_acceleration_2d_graphs()]

    return render_template("graphs.html", sensors_graphs=sensors_graphs)
