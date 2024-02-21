from datetime import datetime, timedelta


def ytt():
    today = datetime.now()
    yesterday = datetime.now() - timedelta(days = 1)
    tomorrow = datetime.now() + timedelta(days = 1)
    return today ,yesterday, tomorrow 