import datetime

def now_datetime() -> datetime.datetime:
        return datetime.datetime.now()
        
def now_time() -> datetime.time:
    return now_datetime().now()

def begin_of_day(date_time: datetime.datetime) -> datetime.datetime:
    return datetime.datetime(
        year=date_time.year,
        month=date_time.month,
        day=date_time.day,
        hour=0,
        minute=0,
        second=0
    )

def end_of_day(date_time: datetime.datetime) -> datetime.datetime:
    return begin_of_day(date_time) + datetime.timedelta(hours=23, minutes=59, seconds=59)

def zero_timedelta() -> datetime.timedelta:
    return datetime.timedelta()

def difference_between_time(time1: datetime.time, time2: datetime.time) -> datetime.timedelta:
    return datetime.timedelta(
        hours = abs(time1.hour-time2.hour),
        minutes = abs(time1.minute-time2.minute),
        seconds = abs(time1.second-time2.second)
    )

def yersteday_of_date(date: datetime.date) -> datetime.date:
    return date-datetime.timedelta(days=1)