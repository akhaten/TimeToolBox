import datetime
import TimeToolBox.Time

def begin_before(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return t.begin.date() < date

def begin_after(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return date < t.begin.date()

def finish_before(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return t.end.date() < date

def finish_after(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return date < t.end.date()

def between(t: TimeToolBox.Time.SimpleTime, start_date: datetime.date, end_date: datetime.date) -> bool:
    return (start_date <= t.begin.date()) and (t.end.date() <= end_date)

def include(date: datetime.date, t: TimeToolBox.Time.SimpleTime) -> bool:
    return (t.begin.date() <= date) and (date <= t.end.date())