from packages.DFRobot_INA219 import INA219
from sensors.sensor_base import SensorBase
from sensors.sensors_config import SensorsConfig
from utils import logs_utils


class CurrentSensor(SensorBase):
    def __init__(self):
        super().__init__()

        self.sensor = None
        self.init_sensor()

        self.name = SensorsConfig.CURRENT_SENSOR_NAME

        self.voltage = 0
        self.current = 0
        self.power = 0

    def init_sensor(self):
        try:
            self.sensor = INA219(1, INA219.INA219_I2C_ADDRESS4)

        except Exception as e:
            logs_utils.log(e)

    def update(self):
        if self.sensor is not None:
            try:
                self.voltage = round(self.sensor.get_bus_voltage_V(), 2)
                self.current = round(self.sensor.get_current_mA(), 2)
                self.power = round(self.sensor.get_power_mW(), 2)

            except Exception as e:
                logs_utils.log(e)

    def get_sensor_values(self):
        values = [self.voltage, self.current, self.power]

        return values

    def parse_sensors_data(self):
        parsed_values = {
            SensorsConfig.SENSOR_NAME_KEY: self.name,
            SensorsConfig.CURRENT_VOLTAGE_VALUE_NAME: self.voltage,
            SensorsConfig.CURRENT_CURRENT_VALUE_NAME: self.current,
            SensorsConfig.CURRENT_POWER_VALUE_NAME: self.power
        }

        return parsed_values
