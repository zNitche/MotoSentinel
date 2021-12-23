from flask import render_template, Blueprint
from __init__ import sensors_handler


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    print(sensors_handler.get_gyro_data())
    return render_template("index.html")
