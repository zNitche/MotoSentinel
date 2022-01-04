class SensorsConfig:
    SENSOR_NAME_KEY = "sensor_name"

    GYRO_SENSOR_NAME = "gyro"

    GYRO_X_VALUE_NAME = "x"
    GYRO_Y_VALUE_NAME = "y"
    GYRO_Z_VALUE_NAME = "z"

    GYRO_VALUES_UNIT = "rad/s"

    ACCELEROMETER_SENSOR_NAME = "accelerometer"

    ACCELEROMETER_X_VALUE_NAME = "x"
    ACCELEROMETER_Y_VALUE_NAME = "y"
    ACCELEROMETER_Z_VALUE_NAME = "z"

    ACCELEROMETER_VALUES_UNIT = "m/s^2"

    TEMP_SENSOR_NAME = "temperature sensor"

    TEMP_TEMPERATURE_VALUE_NAME = "temperature"
    TEMP_HUMIDITY_VALUE_NAME = "humidity"

    TEMP_TEMPERATURE_VALUES_UNIT = "°C"
    TEMP_HUMIDITY_VALUES_UNIT = "%"

    # Graphs
    GRAPH_TIME = "time"

    GRAPH_ACCELERATION = f"acceleration"
    GRAPH_GYRO = f"gyro"

    GRAPH_TEMPERATURE = "temperature"
    GRAPH_HUMIDITY = "humidity"

    ACCELEROMETER_X_VALUE = f"x-axis ({ACCELEROMETER_VALUES_UNIT})"
    ACCELEROMETER_Y_VALUE = f"y-axis ({ACCELEROMETER_VALUES_UNIT})"
    ACCELEROMETER_Z_VALUE = f"z-axis ({ACCELEROMETER_VALUES_UNIT})"

    GYRO_X_VALUE = f"x-axis ({GYRO_VALUES_UNIT})"
    GYRO_Y_VALUE = f"y-axis ({GYRO_VALUES_UNIT})"
    GYRO_Z_VALUE = f"z-axis ({GYRO_VALUES_UNIT})"

    TEMP_TEMPERATURE_VALUE = f"temperature ({TEMP_TEMPERATURE_VALUES_UNIT})"
    TEMP_HUMIDITY_VALUE = f"humidity ({TEMP_HUMIDITY_VALUES_UNIT})"
