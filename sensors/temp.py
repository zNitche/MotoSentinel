import board
import busio
import adafruit_ahtx0
from sensors.sensor_base import SensorBase
from sensors.sensors_config import SensorsConfig
from utils import logs_utils


class Temp(SensorBase):
    def __init__(self):
        super().__init__()

        self.sensor = None
        self.init_sensor()

        self.name = SensorsConfig.TEMP_SENSOR_NAME

        self.temperature = 0
        self.humidity = 0

    def init_sensor(self):
        try:
            self.sensor = adafruit_ahtx0.AHTx0(busio.I2C(board.SCL, board.SDA))
        except Exception as e:
            logs_utils.log(e)

    def update(self):
        if self.sensor is not None:
            try:
                self.temperature = round(self.sensor.temperature, 2)
                self.humidity = round(self.sensor.relative_humidity, 2)
            except Exception as e:
                logs_utils.log(e)

    def get_sensor_values(self):
        values = [self.temperature, self.humidity]

        return values

    def parse_sensors_data(self):
        parsed_values = {
            SensorsConfig.SENSOR_NAME_KEY: self.name,
            SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME: self.temperature,
            SensorsConfig.TEMP_HUMIDITY_VALUE_NAME: self.humidity
        }

        return parsed_values
