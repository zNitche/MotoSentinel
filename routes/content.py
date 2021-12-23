from flask import render_template, Blueprint


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    from app import sensors_manager

    print(sensors_manager.get_gyro_data())

    return render_template("index.html")
