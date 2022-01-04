class SettingsConfig:
    SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME = "acceleration_time_range"
    DEFAULT_ACCELERATION_TIME_RANGE = 60

    SETTINGS_GYRO_TIME_RANGE_KEY_NAME = "gyro_time_range"
    DEFAULT_GYRO_TIME_RANGE = 60

    SETTINGS_TEMP_TIME_RANGE_KEY_NAME = "temp_time_range"
    DEFAULT_TEMP_TIME_RANGE = 60

    SETTINGS_STRUCT = {
        SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME: DEFAULT_ACCELERATION_TIME_RANGE,
        SETTINGS_GYRO_TIME_RANGE_KEY_NAME: DEFAULT_GYRO_TIME_RANGE,
        SETTINGS_TEMP_TIME_RANGE_KEY_NAME: DEFAULT_TEMP_TIME_RANGE
    }

    SETTINGS_PAGE_STRUCT_TITLE_KEY_NAME = "title"
    SETTINGS_PAGE_STRUCT_MODES_KEY_NAME = "modes"
    SETTINGS_PAGE_STRUCT_TIP_KEY_NAME = "tip"

    SETTINGS_PAGE_STRUCT = [
        {
            SETTINGS_PAGE_STRUCT_TITLE_KEY_NAME: "Time Ranges",
            SETTINGS_PAGE_STRUCT_TIP_KEY_NAME: "in minutes",
            SETTINGS_PAGE_STRUCT_MODES_KEY_NAME: [
                SETTINGS_ACCELERATION_TIME_RANGE_KEY_NAME,
                SETTINGS_GYRO_TIME_RANGE_KEY_NAME
            ]
        }
    ]