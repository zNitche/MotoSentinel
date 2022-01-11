from models import Accelerometer, Gyro, Temp


def get_acceleration_data(begin_datetime, end_datetime):
    accelerometer_data = Accelerometer.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in accelerometer_data:
        if begin_datetime <= data.timestamp <= end_datetime:
            timestamps.append(data.timestamp)
            x_values.append(data.x_value)
            y_values.append(data.y_value)
            z_values.append(data.z_value)

    return timestamps, x_values, y_values, z_values


def get_gyro_data(begin_datetime, end_datetime):
    gyro_data = Gyro.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in gyro_data:
        if begin_datetime <= data.timestamp <= end_datetime:
            timestamps.append(data.timestamp)
            x_values.append(data.x_value)
            y_values.append(data.y_value)
            z_values.append(data.z_value)

    return timestamps, x_values, y_values, z_values


def get_temp_data(begin_datetime, end_datetime):
    temp_data = Temp.query.all()

    timestamps = []
    temp_values = []
    humi_values = []

    for data in temp_data:
        if begin_datetime <= data.timestamp <= end_datetime:
            timestamps.append(data.timestamp)
            temp_values.append(data.temp_value)
            humi_values.append(data.humi_value)

    return timestamps, temp_values, humi_values
