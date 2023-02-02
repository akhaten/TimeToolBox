#-------------------------------------------------------------------------------------------------------------------------------

import datetime

#-------------------------------------------------------------------------------------------------------------------------------

import TimeToolBox.Time


#-------------------------------------------------------------------------------------------------------------------------------

# Assertion between events

def begin_before_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 begin before than t2 begin
    '''
    return t1.begin < t2.begin

def begin_after_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 begin after than
    '''
    return t2.begin < t1.begin

def finish_before_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t1.end < t2.begin

def finish_after_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t2.begin < t1.end

def begin_before_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t1.begin < t2.end

def begin_after_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t2.end < t1.begin

def finish_before_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t1.end < t2.end

def finish_after_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return t2.end < t1.end

def between_events(t: TimeToolBox.Time.SimpleTime, t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return begin_after_finish(t, t1) \
        and finish_before_begin(t, t2)

def include(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return begin_after_begin(t1, t2) \
        and finish_after_finish(t1, t2)

def are_parallel(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:

    def collision_without_inclusion(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
        return begin_before_begin(t1, t2) \
            and finish_after_begin(t1, t2) \
            and finish_before_finish(t1, t2)
    
    return collision_without_inclusion(t1, t2) \
        or collision_without_inclusion(t2, t1) \
        or include(t1, t2) \
        or include(t2, t1)


#-------------------------------------------------------------------------------------------------------------------------------

# Assertion between t and datetime.datetime

def begin_before_datetime(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return t.begin < date

def begin_after_datetime(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return date < t.begin

def finish_before_datetime(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return t.end < date

def finish_after_datetime(t: TimeToolBox.Time.SimpleTime, date: datetime.datetime) -> bool:
    return date < t.end

def between_datetime(t: TimeToolBox.Time.SimpleTime, start_datetime: datetime.datetime, end_datetime: datetime.datetime) -> bool:
    return (start_datetime <= t.begin) and (t.end <= end_datetime)

def datetime_include_in(date_time: datetime.datetime, t: TimeToolBox.Time.SimpleTime) -> bool:
    return begin_before_datetime(t, date_time) \
        and finish_after_datetime(t, date_time)

#-------------------------------------------------------------------------------------------------------------------------------

# Assertion between t and datetime.date

def begin_before_date(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return t.begin.date() < date

def begin_after_date(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return date < t.begin.date()

def finish_before_date(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return t.end.date() < date

def finish_after_date(t: TimeToolBox.Time.SimpleTime, date: datetime.date) -> bool:
    return date < t.end.date()

def between_date(t: TimeToolBox.Time.SimpleTime, start_date: datetime.date, end_date: datetime.date) -> bool:
    return (start_date <= t.begin.date()) and (t.end.date() <= end_date)

def date_include_in(date: datetime.date, t: TimeToolBox.Time.SimpleTime) -> bool:
    return (t.begin.date() <= date) and (date <= t.end.date())

#-------------------------------------------------------------------------------------------------------------------------------

# Assertion between t and datetime.time

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

#-------------------------------------------------------------------------------------------------------------------------------

# Other

def include_in_only_a_day(t: TimeToolBox.Time.SimpleTime) -> bool:
    begin_date: datetime.date = t.begin.date()
    end_date: datetime.date = t.end.date()
    return begin_date == end_date