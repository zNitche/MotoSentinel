from flask import render_template, Blueprint
from sensors.sensors_config import SensorsConfig
from utils import graphs_utils, settings_utils
from app_config import AppConfig


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    from app import sensors_manager

    sensors_data = [sensor.parse_sensors_data() for sensor in sensors_manager.get_sensors()]

    return render_template("index.html", sensors_data=sensors_data, sensors_config=SensorsConfig)


@content_.route("/settings")
def settings():
    settings_data = settings_utils.load_settings()

    time_range = AppConfig.DEFAULT_TIME_RANGE

    if len(settings_data.keys()) > 0:
        time_range = settings_data[AppConfig.SETTINGS_TIME_RANGE_KEY_NAME]

    return render_template("settings.html", time_range=time_range)


@content_.route("/graphs")
def graphs():
    acceleration_graphs = graphs_utils.generate_acceleration_2d_graphs()
    gyro_graphs = graphs_utils.generate_gyro_2d_graphs()

    sensors_graphs = [acceleration_graphs, gyro_graphs]

    return render_template("graphs.html", sensors_graphs=sensors_graphs)
