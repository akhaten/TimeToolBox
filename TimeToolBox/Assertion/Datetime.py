import datetime
import TimeToolBox.Time

def begin_before(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return t.begin < date

def begin_after(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return date < t.begin

def finish_before(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return t.end < date

def finish_after(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return date < t.end

def between(t: TimeToolBox.Time.SimpleTime, start_datetime: datetime.datetime, end_datetime: datetime.datetime) -> bool:
    return (start_datetime <= t.begin) and (t.end <= end_datetime)

def include_in(date_time: datetime.datetime, t: TimeToolBox.Time.SimpleTime) -> bool:
    return begin_before(t, date_time) \
        and finish_after(t, date_time)