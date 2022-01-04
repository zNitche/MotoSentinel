import board
import busio
import adafruit_adxl34x
from sensors.sensor_base import SensorBase
from sensors.sensors_config import SensorsConfig
from utils import logs_utils


class Accelerometer(SensorBase):
    def __init__(self):
        super().__init__()

        self.sensor = None
        self.init_sensor()

        self.name = SensorsConfig.ACCELEROMETER_SENSOR_NAME

        self.x_value = 0
        self.y_value = 0
        self.z_value = 0

    def init_sensor(self):
        try:
            self.sensor = adafruit_adxl34x.ADXL345(busio.I2C(board.SCL, board.SDA))
        except Exception as e:
            logs_utils.log(e)

    def update(self):
        if self.sensor is not None:
            try:
                self.x_value = round(self.sensor.acceleration[0], 2)
                self.y_value = round(self.sensor.acceleration[1], 2)
                self.z_value = round(self.sensor.acceleration[2], 2)
            except Exception as e:
                logs_utils.log(e)

    def get_sensor_values(self):
        values = [self.x_value, self.y_value, self.z_value]

        return values

    def parse_sensors_data(self):
        parsed_values = {
            SensorsConfig.SENSOR_NAME_KEY: self.name,
            SensorsConfig.ACCELEROMETER_X_VALUE_NAME: self.x_value,
            SensorsConfig.ACCELEROMETER_Y_VALUE_NAME: self.y_value,
            SensorsConfig.ACCELEROMETER_Z_VALUE_NAME: self.z_value
        }

        return parsed_values
