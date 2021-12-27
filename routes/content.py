from flask import render_template, Blueprint


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    from app import sensors_manager

    sensors_data = [sensor.parse_sensors_data() for sensor in sensors_manager.get_sensors()]

    return render_template("index.html", sensors_data=sensors_data)


@content_.route("/settings")
def settings():
    return "Settings"


@content_.route("/graphs")
def graphs():
    return "Graphs"
