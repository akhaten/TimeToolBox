import datetime
import TimeToolBox.Time

def begin_before_time(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return t.begin.time() < time

def begin_after_time(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return time < t.begin.time()

def finish_before_time(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return t.end.time() < time

def finish_after_time(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return time < t.end.time()

def between_time(t: TimeToolBox.Time.SimpleTime, start_time: datetime.time, end_time: datetime.time) -> bool:
    return (start_time <= t.begin.time()) and (t.end.time() <= end_time)

def time_include_in(time: datetime.time, t: TimeToolBox.Time.SimpleTime) -> bool:
    return (t.begin.time() <= time) and (time <= t.end.time())