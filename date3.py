# Function to drop microseconds from a datetime object
from datetime import datetime


def drop_microseconds(dt):
    return dt.replace(microsecond=0)

current_datetime_with_microseconds = datetime.now()
current_datetime_without_microseconds = drop_microseconds(current_datetime_with_microseconds)


print("Datetime without microseconds: ", current_datetime_without_microseconds)