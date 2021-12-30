from models import Accelerometer, Gyro
import io
import base64
from datetime import datetime, timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from app_config import AppConfig
from utils import settings_utils


def get_acceleration_data(minutes_time_range):
    accelerometer_data = Accelerometer.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in accelerometer_data:
        if datetime.now() - timedelta(minutes=minutes_time_range) <= data.timestamp:
            timestamps.append(data.timestamp)
            x_values.append(data.x_value)
            y_values.append(data.y_value)
            z_values.append(data.z_value)

    return timestamps, x_values, y_values, z_values


def generate_acceleration_2d_graphs():
    graphs = []

    settings_data = settings_utils.load_settings()

    timestamps, x_values, y_values, z_values = get_acceleration_data(settings_data[AppConfig.SETTINGS_TIME_RANGE_KEY_NAME])

    graphs.append(generate_2d_graph(timestamps, x_values, "x-axis acceleration", "time", "acceleration"))
    graphs.append(generate_2d_graph(timestamps, y_values, "y-axis acceleration", "time", "acceleration"))
    graphs.append(generate_2d_graph(timestamps, z_values, "z-axis acceleration", "time", "acceleration"))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def get_gyro_data(minutes_time_range):
    gyro_data = Gyro.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in gyro_data:
        if datetime.now() - timedelta(minutes=minutes_time_range) <= data.timestamp:
            timestamps.append(data.timestamp)
            x_values.append(data.x_value)
            y_values.append(data.y_value)
            z_values.append(data.z_value)

    return timestamps, x_values, y_values, z_values


def generate_gyro_2d_graphs():
    graphs = []

    settings_data = settings_utils.load_settings()

    timestamps, x_values, y_values, z_values = get_gyro_data(settings_data[AppConfig.SETTINGS_TIME_RANGE_KEY_NAME])

    graphs.append(generate_2d_graph(timestamps, x_values, "x-axis gyro", "time", "gyro"))
    graphs.append(generate_2d_graph(timestamps, y_values, "y-axis gyro", "time", "gyro"))
    graphs.append(generate_2d_graph(timestamps, z_values, "z-axis gyro", "time", "gyro"))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def generate_2d_graph(x_points, y_points, title, x_title, y_title):
    fig = Figure()
    fig.set_dpi(AppConfig.GRAPH_DPI_RESOLUTION)

    axis = fig.add_subplot(1, 1, 1)

    axis.set_title(title)
    axis.set_xlabel(x_title)
    axis.set_ylabel(y_title)
    axis.grid()

    axis.plot(x_points, y_points)

    return fig


def encode_graph(fig):
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    encoded_png_string = AppConfig.PNG_ENCODE_STRING
    encoded_png_string += base64.b64encode(png_image.getvalue()).decode("utf8")

    return encoded_png_string
