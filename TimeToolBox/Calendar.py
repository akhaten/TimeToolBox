

import datetime
import typing
import graphviz

import TimeToolBox.Time
import TimeToolBox.Assertion.SimpleTime
import TimeToolBox.Utils.Get




class Day:

    
    class Event:

        def __init__(self, simple_event: TimeToolBox.Time.SimpleEvent, check_collision: bool) -> None:
            self.simple_event: TimeToolBox.Time.SimpleEvent = simple_event
            self.parallel: list[Day.Event] = []
            self.check_collision = check_collision
            self.is_explore = False

        def is_collision(self, simple_event: TimeToolBox.Time.SimpleEvent) -> bool:
            return TimeToolBox.Assertion.SimpleTime.are_parallel(
                self.simple_event, 
                simple_event
            )

        def explore(self) -> tuple[datetime.datetime, datetime.datetime]:

            min_begin = self.simple_event.begin
            max_end = self.simple_event.end
            # print(len(self.parallel))
            for event in self.parallel:
                if not(event.is_explore):
                    event.is_explore = True
                    res_min, res_max = event.explore()
                    # print('ok', min_begin, res_min, min(min_begin, res_min))
                    # print('ok', max_end, res_max, max(max_end, res_max))
                    min_begin = min(min_begin, res_min)
                    max_end = max(max_end, res_max)
                    # print('update', min_begin)
                    # print('update', max_end)


            return min_begin, max_end


        
        # def get_extremum_parallel(self) -> tuple[datetime.datetime, datetime.datetime]:

        #     min_begin = self.simple_event.begin
        #     max_end = self.simple_event.end

        #     if len(self.parallel) == 0:
        #         return min_begin, max_end

        #     for event_parallel in self.parallel:
        #         min_begin = min(event_parallel.simple_event.end, min_begin)
        #         max_end = max(event_parallel.simple_event.end, max_end)
        #         event_parallel.is_explore = True

        #     return min_begin


    def __init__(self, date: datetime.date):
        self.date: datetime.date = date
        self.events: list[Day.Event] = []

    def get_not_free_times(self) -> list[TimeToolBox.Time.SimpleTime]:

        not_free_times: list[TimeToolBox.Time.SimpleTime] = []

        for event in self.events:
            if not(event.is_explore):
                event.is_explore = True
                begin, end = event.explore()
                # print(begin, end)
                not_free_times.append(TimeToolBox.Time.SimpleTime.make(begin, end))

        self.reset_exploration()

        return not_free_times


    def reset_exploration(self) -> None:
        for event in self.events:
            event.is_explore = False
    

    def get_event_parallel(self, simple_event: TimeToolBox.Time.SimpleEvent) -> 'list[Day.Event]':
        parallels: list[Day.Event] = []
        # print(simple_event.begin, simple_event.end)
        # print('Parallel :')
        for event in self.events:
            if event.is_collision(simple_event):
                # print(
                #     event.simple_event.begin,
                #     event.simple_event.end
                # )
                parallels.append(event)

        # print('\n')
        return parallels

    

    def add(self, simple_event: TimeToolBox.Time.SimpleEvent, check_collision: bool) -> bool:

        added: bool = False
        
        parallel = self.get_event_parallel(simple_event)
        # to_add = Day.Event(simple_event, check_collision=True)
        # to_add.parallel = parallel.copy()
        # self.events.append(to_add)

        # for event_parallel in parallel:
        #     event_parallel.parallel.append(to_add)

        # added = True
        # print(parallel)
        # print(to_add.parallel)
        # print(len(to_add.parallel))

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
                # print(parallel)
                # print(to_add.parallel)
                # print(len(to_add.parallel))
        
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
       


    # def export_graph(self) -> graphviz.graphs.Digraph:

    #     graph: graphviz.graphs.Digraph = graphviz.graphs.Digraph(filename=str(self.date))

    #     # for node in self.nodes:
    #     #     event: TimeToolBox.Time.SimpleEvent = node.time
    #     #     e1_exp : TimeToolBox.Time.SimpleEvent = node.time.export()
    #     #     label: str = str(event.infos) + '\n' + str(event.begin) + '\n' + str(event.duration)
    #     #     graph.node(name=str(label), label=label)

     
    #     for node in self.nodes:
    #         node_1: str = str(node.time.infos) + '\n' + str(node.time.begin.time()) + '\n' + str(node.time.end.time())
    #         for neigh in node.parallel:
    #             node_2: str = str(neigh.time.infos) + '\n' + str(neigh.time.begin.time()) + '\n' + str(neigh.time.end.time())
    #             graph.edge(
    #                 tail_name=node_1.replace(':', '-'), 
    #                 head_name=node_2.replace(':', '-')
    #             )

    #     return graph


class SimpleCalendar:


    def __init__(self) -> None:
        self.days: list[Day] = []


    def add(self, time: TimeToolBox.Time.SimpleEvent) -> bool:
        
        date: datetime.date = time.begin.date()
        day_to_add: Day = self.__get_day(date)
        added: bool = day_to_add.add(time)

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


    def __get_day(self, date: datetime.date) -> Day:

        index: int = 0
        
        if self.days == []:
            self.days.append(Day(date))
        else:
            while (index < len(self.days)) and (not find) and (date <= self.days[index].date):
                if self.days[index].date == date:
                    find = True
                else:
                    index += 1
            
        if not find:
            self.days.insert(index, Day(date))
        
        return self.days[index]




    


    