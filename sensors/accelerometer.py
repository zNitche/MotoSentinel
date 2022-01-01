import board
import busio
import adafruit_adxl34x
from sensors.sensor_base import SensorBase
from sensors.sensors_config import SensorsConfig
from utils import logs_utils


class Accelerometer(SensorBase):
    def __init__(self):
        super().__init__()

        self.sensor = adafruit_adxl34x.ADXL345(busio.I2C(board.SCL, board.SDA))
        self.name = SensorsConfig.ACCELEROMETER_SENSOR_NAME

        self.x_value = 0
        self.y_value = 0
        self.z_value = 0

    def update(self):
        try:
            self.x_value = self.sensor.acceleration[0]
            self.y_value = self.sensor.acceleration[1]
            self.z_value = self.sensor.acceleration[2]
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
