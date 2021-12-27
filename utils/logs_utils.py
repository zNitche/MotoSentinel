from utils import processes_utils
from config import Config


def write_log(content):
    with open(Config.LOGS_PATH, "a") as log_file:
        log_content = f"{processes_utils.generate_timestamp()}:{content}\n"

        log_file.write(log_content)


def log(content):
    if Config.DO_LOGS:
        write_log(content)
