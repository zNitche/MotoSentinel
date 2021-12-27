from utils import processes_utils
from app_config import AppConfig


def write_log(content):
    with open(AppConfig.LOGS_PATH, "a") as log_file:
        log_content = f"{processes_utils.generate_timestamp()}:{content}\n"

        log_file.write(log_content)


def log(content):
    if AppConfig.DO_LOGS:
        write_log(content)
