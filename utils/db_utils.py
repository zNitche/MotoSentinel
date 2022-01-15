from models import Accelerometer, Gyro, Temp
from sensors.sensors_config import SensorsConfig


def get_acceleration_data():
    accelerometer_data = Accelerometer.query.all()

    data = []

    for data_row in accelerometer_data:
        row_data = {
            SensorsConfig.TIMESTAMP_NAME_KEY: data_row.timestamp,
            SensorsConfig.ACCELEROMETER_X_VALUE_NAME: data_row.x_value,
            SensorsConfig.ACCELEROMETER_Y_VALUE_NAME: data_row.y_value,
            SensorsConfig.ACCELEROMETER_Z_VALUE_NAME: data_row.z_value
        }

        data.append(row_data)

    return data


def get_gyro_data():
    gyro_data = Gyro.query.all()

    data = []

    for data_row in gyro_data:
        row_data = {
            SensorsConfig.TIMESTAMP_NAME_KEY: data_row.timestamp,
            SensorsConfig.GYRO_X_VALUE_NAME: data_row.x_value,
            SensorsConfig.GYRO_Y_VALUE_NAME: data_row.y_value,
            SensorsConfig.GYRO_Z_VALUE_NAME: data_row.z_value
        }

        data.append(row_data)

    return data


def get_temp_data():
    temp_data = Temp.query.all()

    data = []

    for data_row in temp_data:
        row_data = {
            SensorsConfig.TIMESTAMP_NAME_KEY: data_row.timestamp,
            SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME: data_row.temp_value,
            SensorsConfig.TEMP_HUMIDITY_VALUE_NAME: data_row.humi_value
        }

        data.append(row_data)

    return data


def filter_sensor_data(begin_datetime, end_datetime, sensor_data):
    filtered_data = []

    for row_data in sensor_data:
        if begin_datetime <= row_data[SensorsConfig.TIMESTAMP_NAME_KEY] <= end_datetime:
            filtered_data.append(row_data)

    return filtered_data
