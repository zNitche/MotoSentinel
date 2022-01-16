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


def combine_sensor_data(sensor_data):
    combined_data = {}

    for data_row in sensor_data:
        for data_key in data_row:

            if data_key not in combined_data.keys():
                combined_data[data_key] = []

            combined_data[data_key].append(data_row[data_key])

    return combined_data


def generate_2d_graphs_from_sensor_data(sensor_data):
    graphs = []

    combined_sensor_data = combine_sensor_data(sensor_data)

    for data_collection_key in combined_sensor_data:
        if data_collection_key != SensorsConfig.TIMESTAMP_NAME_KEY:
            graphs.append(generate_2d_graph(combined_sensor_data[SensorsConfig.TIMESTAMP_NAME_KEY],
                                            combined_sensor_data[data_collection_key], SensorsConfig.GRAPHS_TITLES[data_collection_key],
                                            SensorsConfig.GRAPH_TIME,
                                            SensorsConfig.GRAPH_AXIS_TITLES[data_collection_key]))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def generate_acceleration_2d_graphs():
    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_ACCELERATION_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_ACCELERATION_END_TIME_RANGE_KEY_NAME)

    sensor_data = db_utils.filter_sensor_data(begin_time, end_time, db_utils.get_acceleration_data())

    graphs = generate_2d_graphs_from_sensor_data(sensor_data)

    return graphs


def generate_gyro_2d_graphs():
    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_GYRO_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_GYRO_END_TIME_RANGE_KEY_NAME)

    sensor_data = db_utils.filter_sensor_data(begin_time, end_time, db_utils.get_gyro_data())

    graphs = generate_2d_graphs_from_sensor_data(sensor_data)

    return graphs


def generate_temp_2d_graphs():
    begin_time = get_datetime_from_settings(SettingsConfig.SETTINGS_TEMP_BEGIN_TIME_RANGE_KEY_NAME)
    end_time = get_datetime_from_settings(SettingsConfig.SETTINGS_TEMP_END_TIME_RANGE_KEY_NAME)

    sensor_data = db_utils.filter_sensor_data(begin_time, end_time, db_utils.get_temp_data())

    graphs = generate_2d_graphs_from_sensor_data(sensor_data)

    return graphs


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
