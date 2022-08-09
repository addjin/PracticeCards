import datetime


TIMEDATE_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT = "%H:%M:%S"

datetime_object = datetime.datetime

def get_time():
    current_time = datetime_object.now()
    return current_time.strftime(TIME_FORMAT)
