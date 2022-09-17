
import datetime

class Format:

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
        return '{days:%d} {hours:%d}:{minutes:%d}:{second:%d}'.format(days=days, hours=hours, minutes=minutes, seconds=seconds)
        
    def time_from_datetime(date_time: datetime.datetime) -> datetime.time:
        return date_time.time()

    def date_to_datetime(date: datetime.date) -> datetime.datetime:
        return datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day
        )


class Get:

    def now_datetime() -> datetime.datetime:
        return datetime.datetime.now()
        
    def now_time() -> datetime.time:
        return Get.now_datetime().now()

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
        return Get.begin_of_day(date_time) + datetime.timedelta(days=1)

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