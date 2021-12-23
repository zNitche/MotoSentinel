import random


class Gyro:
    def __init__(self):
        self.sensor = None

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
