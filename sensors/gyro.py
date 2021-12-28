import random
from sensors.sensor_base import SensorBase


class Gyro(SensorBase):
    def __init__(self):
        super().__init__()

        self.sensor = None
        self.name = "Gyro"

        self.x_value = 0
        self.y_value = 0
        self.z_value = 0

    def update(self):
        # TMP Mock

        self.x_value = random.randint(0, 10)
        self.y_value = random.randint(0, 10)
        self.z_value = random.randint(0, 10)

    def get_sensor_values(self):
        values = [self.x_value, self.y_value, self.z_value]

        return values

    def parse_sensors_data(self):
        parsed_values = {
            "sensor_name": self.name,
            "x": self.x_value,
            "y": self.y_value,
            "z": self.z_value
        }

        return parsed_values
