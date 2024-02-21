from datetime import datetime, timedelta

#subtracts 5 days
def subtract_five_days():
    return datetime.now() - timedelta(days = 5)

now = subtract_five_days()
print(now)