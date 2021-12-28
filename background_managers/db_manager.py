import multiprocessing
import time
from models import Gyro, Accelerometer
from utils import processes_utils
from background_managers.managers_config import ManagersConfig


class DBManager:
    def __init__(self, app, db, sensors_manager):
        self.app = app
        self.database = db
        self.sensors_manager = sensors_manager

        self.is_running = False
        self.process = multiprocessing.Process(target=self.mainloop)

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

    def generate_gyro_data(self):
        gyro_data = self.sensors_manager.get_sensor_data_by_sensor_name("gyro")

        gyro = Gyro(timestamp=processes_utils.generate_timestamp(), x_value=gyro_data[0], y_value=gyro_data[1],
                    z_value=gyro_data[2])

        return gyro

    def generate_accelerometer_data(self):
        accelerometer_data = self.sensors_manager.get_sensor_data_by_sensor_name("accelerometer")

        accelerometer = Accelerometer(timestamp=processes_utils.generate_timestamp(), x_value=accelerometer_data[0],
                                      y_value=accelerometer_data[1], z_value=accelerometer_data[2])

        return accelerometer
