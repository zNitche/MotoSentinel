from datetime import datetime


class SettingsConfig:
    TIMEDATE_STR = "%Y-%m-%dT%H:%M"

    SETTINGS_ACCELERATION_BEGIN_TIME_RANGE_KEY_NAME = "acceleration_begin_time_range"
    DEFAULT_ACCELERATION_BEGIN_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_GYRO_BEGIN_TIME_RANGE_KEY_NAME = "gyro_begin_time_range"
    DEFAULT_GYRO_BEGIN_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_TEMP_BEGIN_TIME_RANGE_KEY_NAME = "temp_begin_time_range"
    DEFAULT_TEMP_BEGIN_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_ACCELERATION_END_TIME_RANGE_KEY_NAME = "acceleration_end_time_range"
    DEFAULT_ACCELERATION_END_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_GYRO_END_TIME_RANGE_KEY_NAME = "gyro_end_time_range"
    DEFAULT_GYRO_END_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_TEMP_END_TIME_RANGE_KEY_NAME = "temp_end_time_range"
    DEFAULT_TEMP_END_TIME_RANGE = datetime.now().strftime(TIMEDATE_STR)

    SETTINGS_STRUCT = {
        SETTINGS_ACCELERATION_BEGIN_TIME_RANGE_KEY_NAME: DEFAULT_ACCELERATION_BEGIN_TIME_RANGE,
        SETTINGS_GYRO_BEGIN_TIME_RANGE_KEY_NAME: DEFAULT_GYRO_BEGIN_TIME_RANGE,
        SETTINGS_TEMP_BEGIN_TIME_RANGE_KEY_NAME: DEFAULT_TEMP_BEGIN_TIME_RANGE,
        SETTINGS_ACCELERATION_END_TIME_RANGE_KEY_NAME: DEFAULT_ACCELERATION_END_TIME_RANGE,
        SETTINGS_GYRO_END_TIME_RANGE_KEY_NAME: DEFAULT_GYRO_END_TIME_RANGE,
        SETTINGS_TEMP_END_TIME_RANGE_KEY_NAME: DEFAULT_TEMP_END_TIME_RANGE
    }

    SETTINGS_PAGE_STRUCT_TITLE_KEY_NAME = "title"
    SETTINGS_PAGE_STRUCT_MODES_ITEMS = "modes"
    SETTINGS_PAGE_STRUCT_TIP_KEY_NAME = "tip"

    SETTINGS_ITEM_NAME = "item_name"
    SETTINGS_ITEM_INPUT_TYPE = "input_type"

    TEXT_INPUT_TYPE = "text"
    DATETIME_INPUT_TYPE = "datetime-local"

    SETTINGS_PAGE_STRUCT = [
        {
            SETTINGS_PAGE_STRUCT_TITLE_KEY_NAME: "Time Ranges",
            SETTINGS_PAGE_STRUCT_TIP_KEY_NAME: "Dates Ranges",
            SETTINGS_PAGE_STRUCT_MODES_ITEMS: [
                {
                    SETTINGS_ITEM_NAME: SETTINGS_ACCELERATION_BEGIN_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                },
                {
                    SETTINGS_ITEM_NAME: SETTINGS_ACCELERATION_END_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                },
                {
                    SETTINGS_ITEM_NAME: SETTINGS_GYRO_BEGIN_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                },
                {
                    SETTINGS_ITEM_NAME: SETTINGS_GYRO_END_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                },
                {
                    SETTINGS_ITEM_NAME: SETTINGS_TEMP_BEGIN_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                },
                {
                    SETTINGS_ITEM_NAME: SETTINGS_TEMP_END_TIME_RANGE_KEY_NAME,
                    SETTINGS_ITEM_INPUT_TYPE: DATETIME_INPUT_TYPE
                }
            ]
        }
    ]
