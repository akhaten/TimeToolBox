import datetime
import TimeToolBox.Time

def begin_before(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return t.begin.time() < time

def begin_after(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return time < t.begin.time()

def finish_before(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return t.end.time() < time

def finish_after(t: TimeToolBox.Time.SimpleTime, time: datetime.time) -> bool:
    return time < t.end.time()

def between(t: TimeToolBox.Time.SimpleTime, start_time: datetime.time, end_time: datetime.time) -> bool:
    return (start_time <= t.begin.time()) and (t.end.time() <= end_time)

def include_in(time: datetime.time, t: TimeToolBox.Time.SimpleTime) -> bool:
    return (t.begin.time() <= time) and (time <= t.end.time())