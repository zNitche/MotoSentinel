import threading
import time
from sensors.gyro import Gyro


class SensorHandler:
    def __init__(self):
        self.is_running = False
        self.process = threading.Thread(target=self.mainloop)

        self.gyro_sensor = Gyro()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.process.start()

    def mainloop(self):
        while self.is_running:
            self.gyro_sensor.update()
            #print(self.get_gyro_data())

            time.sleep(0.5)

    def get_gyro_data(self):
        return self.gyro_sensor.get_sensor_values()
