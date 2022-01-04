from models import Accelerometer, Gyro, Temp
import io
import base64
from datetime import datetime, timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from app_config import AppConfig
from settings_config import SettingsConfig
from sensors.sensors_config import SensorsConfig
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

    timestamps, x_values, y_values, z_values = get_acceleration_data(settings_data[SettingsConfig.SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME])

    graphs.append(generate_2d_graph(timestamps, x_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_X_VALUE))
    graphs.append(generate_2d_graph(timestamps, y_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_Y_VALUE))
    graphs.append(generate_2d_graph(timestamps, z_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_Z_VALUE))

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

    timestamps, x_values, y_values, z_values = get_gyro_data(settings_data[SettingsConfig.SETTINGS_GYRO_TIME_RANGE_KEY_NAME])

    graphs.append(generate_2d_graph(timestamps, x_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_X_VALUE))
    graphs.append(generate_2d_graph(timestamps, y_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_Y_VALUE))
    graphs.append(generate_2d_graph(timestamps, z_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_Z_VALUE))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def get_temp_data(minutes_time_range):
    temp_data = Temp.query.all()

    timestamps = []
    temp_values = []
    humi_values = []

    for data in temp_data:
        if datetime.now() - timedelta(minutes=minutes_time_range) <= data.timestamp:
            timestamps.append(data.timestamp)
            temp_values.append(data.temp_value)
            humi_values.append(data.humi_value)

    return timestamps, temp_values, humi_values


def generate_temp_2d_graphs():
    graphs = []

    settings_data = settings_utils.load_settings()

    timestamps, temp_values, humi_values = get_temp_data(settings_data[SettingsConfig.SETTINGS_TEMP_TIME_RANGE_KEY_NAME])

    graphs.append(generate_2d_graph(timestamps, temp_values, SensorsConfig.GRAPH_TEMPERATURE, SensorsConfig.GRAPH_TIME, SensorsConfig.TEMP_TEMPERATURE_VALUE))
    graphs.append(generate_2d_graph(timestamps, humi_values, SensorsConfig.GRAPH_HUMIDITY, SensorsConfig.GRAPH_TIME, SensorsConfig.TEMP_HUMIDITY_VALUE))

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
