import threading
import time
from datetime import datetime
from models import Gyro, Accelerometer
from background_managers.managers_config import ManagersConfig
from sensors.sensors_config import SensorsConfig


class DBManager:
    def __init__(self, app, db, sensors_manager):
        self.app = app
        self.database = db
        self.sensors_manager = sensors_manager

        self.is_running = False
        self.process = threading.Thread(target=self.mainloop)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.process.start()

    def mainloop(self):
        while self.is_running:
            with self.app.app_context():
                self.database.session.add(self.generate_gyro_data())
                self.database.session.add(self.generate_accelerometer_data())

                self.database.session.commit()

            time.sleep(ManagersConfig.DB_MANAGER_UPDATE_RATE)
            print("updating mainloop")

    def generate_gyro_data(self):
        gyro_data = self.sensors_manager.get_sensor_parsed_data_by_sensor_name(SensorsConfig.GYRO_SENSOR_NAME)

        gyro = Gyro(timestamp=datetime.now(),
                    x_value=gyro_data[SensorsConfig.GYRO_X_VALUE_NAME],
                    y_value=gyro_data[SensorsConfig.GYRO_Y_VALUE_NAME],
                    z_value=gyro_data[SensorsConfig.GYRO_Z_VALUE_NAME])

        return gyro

    def generate_accelerometer_data(self):
        accelerometer_data = self.sensors_manager.get_sensor_parsed_data_by_sensor_name(SensorsConfig.ACCELEROMETER_SENSOR_NAME)

        accelerometer = Accelerometer(timestamp=datetime.now(),
                                      x_value=accelerometer_data[SensorsConfig.ACCELEROMETER_X_VALUE_NAME],
                                      y_value=accelerometer_data[SensorsConfig.ACCELEROMETER_Y_VALUE_NAME],
                                      z_value=accelerometer_data[SensorsConfig.ACCELEROMETER_Z_VALUE_NAME])

        return accelerometer
