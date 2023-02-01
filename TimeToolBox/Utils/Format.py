import datetime

def datetime_to_string(date_time: datetime.datetime) -> str:
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def date_to_string(date: datetime.date) -> str:
    return date.strftime('%Y-%m-%d')

def string_to_datetime(date_time_str: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(date_time_str)

def timedelta_to_string(time_delta: datetime.timedelta) -> str:
    days: int = time_delta.days
    hours: int = time_delta.seconds % 3600
    seconds: int = time_delta.seconds-hours*3600
    minutes: int =  seconds % 60
    seconds: int = seconds-minutes*60
    str_format: str = '{days:%d} {hours:%d}:{minutes:%d}:{second:%d}'
    return str_format.format(
        days=days,
        hours=hours,
        minutes=minutes, 
        seconds=seconds
    )
    
def time_from_datetime(date_time: datetime.datetime) -> datetime.time:
    return date_time.time()

def date_to_datetime(date: datetime.date) -> datetime.datetime:
    return datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day
    )