import datetime
import TimeToolBox.Time

def begin_before_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 starts before t2 starts
    '''
    return t1.begin < t2.begin

def begin_after_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 starts after t2 starts
    '''
    return t2.begin < t1.begin

def finish_before_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 finishes before t2 starts
    '''
    return t1.end < t2.begin

def finish_after_begin(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 finishes after t2 starts
    '''
    return t2.begin < t1.end

def begin_before_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 starts before t2 finishes
    '''
    return t1.begin < t2.end

def begin_after_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 starts after t2 finishes
    '''
    return t2.end < t1.begin

def finish_before_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 finishes before t2 finishes
    '''
    return t1.end < t2.end

def finish_after_finish(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t1 finishes after t2 finishes
    '''
    return t2.end < t1.end

def between(t: TimeToolBox.Time.SimpleTime, t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    ''' t finishes after t2 finishes
    '''
    return begin_after_finish(t, t1) \
        and finish_before_begin(t, t2)

def include(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
    return begin_after_begin(t1, t2) \
        and finish_after_finish(t1, t2)

def are_parallel(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:

    def collision(t1: TimeToolBox.Time.SimpleTime, t2: TimeToolBox.Time.SimpleTime) -> bool:
        return finish_after_begin(t1, t2) \
            and finish_before_finish(t1, t2)

        # return begin_before_begin(t1, t2) \
        #     and finish_after_begin(t1, t2) \
        #     and finish_before_finish(t1, t2)
    
    return collision(t1, t2) \
        or collision(t2, t1)
        # or include(t1, t2) \
        # or include(t2, t1)

def include_in_only_a_day(t: TimeToolBox.Time.SimpleTime) -> bool:
    begin_date: datetime.date = t.begin.date()
    end_date: datetime.date = t.end.date()
    return begin_date == end_date