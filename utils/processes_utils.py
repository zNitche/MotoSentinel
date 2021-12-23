from datetime import datetime


def generate_timestamp():
    timestamp = datetime.now()

    timestamp = str(timestamp).replace(" ", "_")
    timestamp = str(timestamp).replace(".", "_")

    return timestamp
