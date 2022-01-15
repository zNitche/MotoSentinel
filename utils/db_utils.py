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


def filter_acceleration_data(begin_datetime, end_datetime, accelerometer_data):
    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for row_data in accelerometer_data:
        if begin_datetime <= row_data[SensorsConfig.TIMESTAMP_NAME_KEY] <= end_datetime:
            timestamps.append(row_data[SensorsConfig.TIMESTAMP_NAME_KEY])
            x_values.append(row_data[SensorsConfig.ACCELEROMETER_X_VALUE_NAME])
            y_values.append(row_data[SensorsConfig.ACCELEROMETER_Y_VALUE_NAME])
            z_values.append(row_data[SensorsConfig.ACCELEROMETER_Z_VALUE_NAME])

    return timestamps, x_values, y_values, z_values


def filter_gyro_data(begin_datetime, end_datetime, gyro_data):
    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for row_data in gyro_data:
        if begin_datetime <= row_data[SensorsConfig.TIMESTAMP_NAME_KEY] <= end_datetime:
            timestamps.append(row_data[SensorsConfig.TIMESTAMP_NAME_KEY])
            x_values.append(row_data[SensorsConfig.GYRO_X_VALUE_NAME])
            y_values.append(row_data[SensorsConfig.GYRO_Y_VALUE_NAME])
            z_values.append(row_data[SensorsConfig.GYRO_Z_VALUE_NAME])

    return timestamps, x_values, y_values, z_values


def filter_temp_data(begin_datetime, end_datetime, temp_data):
    timestamps = []
    temp_values = []
    humi_values = []

    for row_data in temp_data:
        if begin_datetime <= row_data[SensorsConfig.TIMESTAMP_NAME_KEY] <= end_datetime:
            timestamps.append(row_data[SensorsConfig.TIMESTAMP_NAME_KEY])
            temp_values.append(row_data[SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME])
            humi_values.append(row_data[SensorsConfig.TEMP_HUMIDITY_VALUE_NAME])

    return timestamps, temp_values, humi_values
