import multiprocessing
import time
from models import Gyro
from utils import processes_utils


class DBHandler:
    def __init__(self, app, db, sensors_handler):
        self.app = app
        self.database = db
        self.sensors_handler = sensors_handler

        self.is_running = False
        self.process = multiprocessing.Process(target=self.mainloop)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.process.start()

    def mainloop(self):
        while self.is_running:
            gyro_data = self.sensors_handler.get_gyro_data()
            gyro = Gyro(timestamp=processes_utils.generate_timestamp(), x_value=gyro_data[0], y_value=gyro_data[1],
                        z_value=gyro_data[2])

            with self.app.app_context():
                print("Update...")

                self.database.session.add(gyro)

                self.database.session.commit()

            time.sleep(1)
