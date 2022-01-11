import io
import base64
from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from app_config import AppConfig
from settings_config import SettingsConfig
from sensors.sensors_config import SensorsConfig
from utils import settings_utils, db_utils


def get_datetime_from_settings(settings_key_name):
    settings_data = settings_utils.load_settings()

    date_time = datetime.strptime(settings_data[settings_key_name], SettingsConfig.TIMEDATE_STR)

    return date_time


def generate_acceleration_2d_graphs():
    graphs = []

    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_ACCELERATION_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_ACCELERATION_END_TIME_RANGE_KEY_NAME)

    timestamps, x_values, y_values, z_values = db_utils.filter_acceleration_data(begin_time, end_time, db_utils.get_acceleration_data())

    graphs.append(generate_2d_graph(timestamps, x_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_X_VALUE))
    graphs.append(generate_2d_graph(timestamps, y_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_Y_VALUE))
    graphs.append(generate_2d_graph(timestamps, z_values, SensorsConfig.GRAPH_ACCELERATION, SensorsConfig.GRAPH_TIME, SensorsConfig.ACCELEROMETER_Z_VALUE))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def generate_gyro_2d_graphs():
    graphs = []

    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_GYRO_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_GYRO_END_TIME_RANGE_KEY_NAME)

    timestamps, x_values, y_values, z_values = db_utils.filter_gyro_data(begin_time, end_time, db_utils.get_gyro_data())

    graphs.append(generate_2d_graph(timestamps, x_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_X_VALUE))
    graphs.append(generate_2d_graph(timestamps, y_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_Y_VALUE))
    graphs.append(generate_2d_graph(timestamps, z_values, SensorsConfig.GRAPH_GYRO, SensorsConfig.GRAPH_TIME, SensorsConfig.GYRO_Z_VALUE))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def generate_temp_2d_graphs():
    graphs = []

    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_TEMP_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_TEMP_END_TIME_RANGE_KEY_NAME)

    timestamps, temp_values, humi_values = db_utils.filter_temp_data(begin_time, end_time, db_utils.get_temp_data())

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
