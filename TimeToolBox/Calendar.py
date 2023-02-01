

import datetime
import typing
import graphviz

import TimeToolBox.Time
import TimeToolBox.Assertion
import TimeToolBox.Utils



class Day:

        
    class Node:

        def __init__(self, time: TimeToolBox.Time.SimpleEvent) -> None:
            self.time: TimeToolBox.Time.SimpleEvent = time
            self.parallel: list[Day.Node] = []

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, TimeToolBox.Time.SimpleEvent):
                return False
            return other == self.time
        


    def __init__(self, date: datetime.date):
        self.date: datetime.date = date
        self.nodes: list[Day.Node] = []
    

    def add(self, time: TimeToolBox.Time.SimpleEvent, check_collision: bool = False) -> bool:

        added: bool = False
        new_node: Day.Node = Day.Node(time)
        parallels: list[TimeToolBox.Time.SimpleEvent] = []

        for node in self.nodes:
            if TimeToolBox.Assertion.are_parallel(new_node.time, node.time):
                parallels.append(node)

        if (check_collision and (parallels == [])) \
            or (not check_collision):

            for node in self.nodes:
                node.parallel.append(new_node)
            new_node.parallel = parallels
            self.nodes.append(new_node)
            added = True
        
        return added

    
    def remove(self, time: TimeToolBox.Time.SimpleEvent) -> bool:

        if not(time in self.nodes):
            return False

        for index in range(0, len(self.nodes)):

            node: Day.Node = self.nodes[index]
            
            if node.time == time:
                index_to_remove = index
            else:
                node.parallel.remove(node)

        self.nodes.pop(index_to_remove)

        return True


    def get_free_times(self) -> list[TimeToolBox.Time.SimpleTime]:
                
        not_free_times: list[TimeToolBox.Time.SimpleTime] = self.__get_not_free_time()
        not_free_times: list[TimeToolBox.Time.SimpleTime] = sorted(not_free_times, key=lambda e : e.begin)

        free_times: list[TimeToolBox.Time.SimpleTime] = []

        begin: datetime.datetime = TimeToolBox.Utils.Get.begin_of_day(self.date)
        end: datetime.datetime = not_free_times[0].begin
        free_times.append(TimeToolBox.Time.SimpleTime.make(begin, end))

        for index in range(len(not_free_times)-1):
            t1: TimeToolBox.Time.SimpleTime = not_free_times[index]
            t2: TimeToolBox.Time.SimpleTime = not_free_times[index+1]
            free_times.append(TimeToolBox.Time.SimpleTime.make(t1.end, t2.begin))

        begin: datetime.datetime = not_free_times[len(not_free_times)-1].end
        end: datetime.datetime = TimeToolBox.Utils.Get.end_of_day(self.date)
        free_times.append(TimeToolBox.Time.SimpleTime.make(begin, end))

        return free_times
        # return self.__get_not_free_time()


    def __get_not_free_time(self) -> list[TimeToolBox.Time.SimpleTime]:

        visited: list[TimeToolBox.Time.SimpleTime] = []
        not_free_times: list[TimeToolBox.Time.SimpleTime] = []


        def update(current: TimeToolBox.Time.SimpleTime, acc: TimeToolBox.Time.SimpleTime) -> TimeToolBox.Time.SimpleEvent :
            begin: datetime.datetime = min(current.begin, acc.begin)
            end: datetime.datetime = max(current.end, acc.end)
            nft: TimeToolBox.Time.SimpleTime = TimeToolBox.Time.SimpleTime.make(begin, end)
            # print()
            # print("acc :", acc.begin, acc.end)
            # print("current :", current.begin, current.end)
            # print()
            return nft
        

        def explore(node: Day.Node, acc: TimeToolBox.Time.SimpleTime) -> TimeToolBox.Time.SimpleTime:
            visited.append(node.time)
            acc: TimeToolBox.Time.SimpleTime = update(node.time, acc)
            # print("acc updated", acc.begin, acc.end)
            for neigh in node.parallel:
                if not(neigh.time in visited):
                    acc: TimeToolBox.Time.SimpleTime = explore(neigh, acc)
            return acc


        for node in self.nodes:
            if not(node.time in visited):
                acc: TimeToolBox.Time.SimpleTime = TimeToolBox.Time.SimpleTime.copy(node.time)
                res: TimeToolBox.Time.SimpleTime = explore(node, acc)
                not_free_times.append(res)
                # print("acc added", res.begin, res.end)


        return not_free_times


    def export_graph(self) -> graphviz.graphs.Digraph:

        graph: graphviz.graphs.Digraph = graphviz.graphs.Digraph(filename=str(self.date))

        # for node in self.nodes:
        #     event: TimeToolBox.Time.SimpleEvent = node.time
        #     e1_exp : TimeToolBox.Time.SimpleEvent = node.time.export()
        #     label: str = str(event.infos) + '\n' + str(event.begin) + '\n' + str(event.duration)
        #     graph.node(name=str(label), label=label)

     
        for node in self.nodes:
            node_1: str = str(node.time.infos) + '\n' + str(node.time.begin.time()) + '\n' + str(node.time.end.time())
            for neigh in node.parallel:
                node_2: str = str(neigh.time.infos) + '\n' + str(neigh.time.begin.time()) + '\n' + str(neigh.time.end.time())
                graph.edge(
                    tail_name=node_1.replace(':', '-'), 
                    head_name=node_2.replace(':', '-')
                )

        return graph


class SimpleCalendar:


    def __init__(self) -> None:
        self.days: list[Day] = []


    def add(self, time: TimeToolBox.Time.SimpleEvent) -> bool:
        date: datetime.date = time.begin.date()
        day_to_add: Day = self.__search_day(date)
        added: bool = day_to_add.add(time)
        return added


    def remove(self, time: TimeToolBox.Time.SimpleEvent) -> bool:
        date: datetime.date = time.begin.date()
        day_to_add: Day = self.__search_day(date)
        added: bool = day_to_add.remove(time)
        return added


    def __search_day(self, date: datetime.date) -> Day:

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




    


    