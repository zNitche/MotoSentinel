from flask import render_template, Blueprint, current_app
from sensors.sensors_config import SensorsConfig
from utils import graphs_utils, settings_utils
from settings_config import SettingsConfig


content = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content.route("/")
def home():
    sensors_manager = current_app.sensors_manager

    sensors_data = [sensor.parse_sensors_data() for sensor in sensors_manager.get_sensors()]

    return render_template("index.html", sensors_data=sensors_data, sensors_config=SensorsConfig)


@content.route("/settings")
def settings():
    settings_data = settings_utils.load_settings()

    return render_template("settings.html", settings_data=settings_data, settings_config=SettingsConfig)


@content.route("/graphs")
def graphs():
    acceleration_graphs = graphs_utils.generate_acceleration_2d_graphs()
    gyro_graphs = graphs_utils.generate_gyro_2d_graphs()
    temp_graphs = graphs_utils.generate_temp_2d_graphs()
    current_graphs = graphs_utils.generate_current_2d_graphs()

    sensors_graphs = [acceleration_graphs, gyro_graphs, temp_graphs, current_graphs]

    return render_template("graphs.html", sensors_graphs=sensors_graphs)
