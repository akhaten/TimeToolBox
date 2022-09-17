
import sys
import datetime
import graphviz

sys.path.append('.')

import TimeToolBox.Calendar
import TimeToolBox.Time


class Information(TimeToolBox.Time.SimpleEvent.AbstractInformation):


    def __init__(self, name: str) -> None:
        self.name: str = name


    def export(self) -> dict:
        return { 'name' : self.name }


    def __eq__(self, other: "Information") -> bool:
        return self.name == other.name


    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':

    valorant: TimeToolBox.Time.SimpleEvent = TimeToolBox.Time.SimpleEvent(
        infos = Information(name='Valorant'),
        begin = datetime.datetime(year=2022, month=1, day=1, hour=7, minute=0),
        duration = datetime.timedelta(hours=3)
    )

    league_of_legends: TimeToolBox.Time.SimpleEvent = TimeToolBox.Time.SimpleEvent(
        infos = Information(name='League Of Legends'),
        begin = datetime.datetime(year=2022, month=1, day=1, hour=9, minute=0),
        duration = datetime.timedelta(hours=3)
    )

    valorant2: TimeToolBox.Time.SimpleEvent = TimeToolBox.Time.SimpleEvent(
        infos = Information(name='Valorant'),
        begin = datetime.datetime(year=2022, month=1, day=1, hour=14, minute=0),
        duration = datetime.timedelta(hours=3)
    )

    day: TimeToolBox.Calendar.Day = TimeToolBox.Calendar.Day(
        date = valorant.begin.date()
    )

    day.add(
        TimeToolBox.Time.SimpleEvent(
            infos = Information(name='Valorant'),
            begin = datetime.datetime(year=2022, month=1, day=1, hour=7, minute=0),
            duration = datetime.timedelta(hours=3)
        )
    )


    day.add(
            TimeToolBox.Time.SimpleEvent(
            infos = Information(name='League Of Legends'),
            begin = datetime.datetime(year=2022, month=1, day=1, hour=9, minute=0),
            duration = datetime.timedelta(hours=3)
        )
    )


    day.add(
        TimeToolBox.Time.SimpleEvent(
            infos = Information(name='Valorant'),
            begin = datetime.datetime(year=2022, month=1, day=1, hour=14, minute=0),
            duration = datetime.timedelta(hours=3)
        )
    )


    graph: graphviz.graphs.Digraph = day.export_graph()

    # graph.render(view=True)
    graph.save(directory='tests/Calendar')
    graph.render(directory='tests/Calendar')

    free_time: list[TimeToolBox.Time.SimpleTime] = day.get_free_times()

    # for ft in free_time:
    #     print(ft.begin, ft.end)


