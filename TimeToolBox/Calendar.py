

import datetime
import typing

import TimeToolBox.Time
import TimeToolBox.Assertion.SimpleTime
import TimeToolBox.Utils.Get



class Day:


    class Event:

        def __init__(self, simple_event: TimeToolBox.Time.SimpleEvent, check_collision: bool = False) -> None:
            self.simple_event: TimeToolBox.Time.SimpleEvent = simple_event
            self.parallel: list[Day.Event] = []
            self.check_collision = check_collision


    class EventNode(Event):

        def __init__(self, simple_event: TimeToolBox.Time.SimpleEvent, check_collision: bool = False) -> None:
            Day.Event.__init__(self, simple_event, check_collision)
            self.is_explore = False

        def is_collision(self, simple_event: TimeToolBox.Time.SimpleEvent) -> bool:
            return TimeToolBox.Assertion.SimpleTime.are_parallel(
                self.simple_event, 
                simple_event
            )

        def explore(self) -> tuple[datetime.datetime, datetime.datetime]:

            min_begin = self.simple_event.begin
            max_end = self.simple_event.end

            for event in self.parallel:
                current_explore: Day.EventNode = event
                if not(current_explore.is_explore):
                    current_explore.is_explore = True
                    res_min, res_max = current_explore.explore()
                    min_begin = min(min_begin, res_min)
                    max_end = max(max_end, res_max)

            return min_begin, max_end


    def __init__(self, date: datetime.date):
        self.date: datetime.date = date
        self.events: list[Day.EventNode] = []

    def get_not_free_times(self) -> list[TimeToolBox.Time.SimpleTime]:

        not_free_times: list[TimeToolBox.Time.SimpleTime] = []

        for event in self.events:
            if not(event.is_explore):
                event.is_explore = True
                begin, end = event.explore()
                not_free_times.append(TimeToolBox.Time.SimpleTime.make(begin, end))

        self.reset_exploration()

        return not_free_times


    def reset_exploration(self) -> None:
        for event in self.events:
            event.is_explore = False
    

    def get_event_parallel(self, simple_event: TimeToolBox.Time.SimpleEvent) -> 'list[Day.EventNode]':
        parallels: list[Day.EventNode] = []
    
        for event in self.events:
            if event.is_collision(simple_event):
                parallels.append(event)

        return parallels

    

    def add(self, simple_event: TimeToolBox.Time.SimpleEvent, check_collision: bool = False) -> bool:

        added: bool = False
        
        parallel = self.get_event_parallel(simple_event)

        if check_collision == False:
            
            to_add = Day.Event(simple_event, check_collision=False)
            to_add.parallel = parallel.copy()
            self.events.append(to_add)

            for event_parallel in parallel:
                event_parallel.parallel.append(to_add)


            added = True


        else:

            if len(parallel) != 0:
                
                added = False
            
            else:

                to_add = Day.Event(simple_event, check_collision=True)
                to_add.parallel = parallel.copy()
                self.events.append(to_add)

                for event_parallel in parallel:
                    event_parallel.parallel.append(to_add)

                added = True
        
        return added

    
    # def remove(self, simple_time: TimeToolBox.Time.SimpleEvent) -> bool:



    #     if not(time in self.nodes):
    #         return False

    #     for index in range(0, len(self.nodes)):

    #         node: Day.Node = self.nodes[index]
            
    #         if node.time == time:
    #             index_to_remove = index
    #         else:
    #             node.parallel.remove(node)

    #     self.nodes.pop(index_to_remove)

    #     return True

   
    # def get_free_times(self) -> list[TimeToolBox.Time.SimpleTime]:

        




    def get_free_times(self) -> list[TimeToolBox.Time.SimpleTime]:
                
        not_free_times: list[TimeToolBox.Time.SimpleTime] = self.get_not_free_times()
        not_free_times.sort(key=lambda e : e.begin)

        free_times: list[TimeToolBox.Time.SimpleTime] = []


        for index in range(len(not_free_times)-1):
            t1: TimeToolBox.Time.SimpleTime = not_free_times[index]
            t2: TimeToolBox.Time.SimpleTime = not_free_times[index+1]
            free_times.append(TimeToolBox.Time.SimpleTime.make(t1.end, t2.begin))


        begin_day = TimeToolBox.Utils.Get.begin_of_day(self.date)
        if begin_day < not_free_times[0].begin:
            free_times.insert(
                0,
                TimeToolBox.Time.SimpleTime.make(
                    begin_day,
                    not_free_times[0].begin,
                )
            )

        n = len(not_free_times)

        end_day = TimeToolBox.Utils.Get.end_of_day(self.date)
        if not_free_times[n-1].end < end_day:
            free_times.append(
                TimeToolBox.Time.SimpleTime.make(
                    not_free_times[n-1].end,
                    end_day,
                )
            )

        return free_times


class SimpleCalendar:


    def __init__(self) -> None:
        self.days: list[Day] = []


    def add(self, simple_event: TimeToolBox.Time.SimpleEvent) -> bool:
        
        date: datetime.date = simple_event.begin.date()
        day = self.create_day(date) if not(self.day_exists(date)) else self.get_day(date)
        day.add(simple_event, True)
        added: bool = day.add(simple_event)

        return added


    # def remove(self, time: TimeToolBox.Time.SimpleEvent) -> bool:

    #     date: datetime.date = time.begin.date()
    #     day_to_add: Day = self.__get_day(date)
    #     added: bool = day_to_add.remove(time)
        
    #     return added


    def day_exists(self, date: datetime.date) -> bool:
        for day in self.days:
            if day.date == date:
                return True
        return False


    def get_events(self, date: datetime.date) -> list[TimeToolBox.Time.SimpleEvent] :
        day = self.get_day(date)
        return [ day_event.simple_event for day_event in day.events ]


    
    def create_day(self, date: datetime.date) -> Day:

        index: int = 0

        day_created = Day(date)
        
        if self.days == []:
            self.days.append(day_created)
        else:
            while (index < len(self.days)) and (date <= self.days[index].date):
                index += 1
            
        
        self.days.insert(index, day_created)

        return day_created
    

    def get_day(self, date: datetime.date) -> Day:

        for day in self.days:
            if day.date == date:
                return date
            
        raise AssertionError("Day not found")




    


    