#-------------------------------------------------------------------------------------------------------------------------------

import unittest
import sys
import datetime
import abc

#-------------------------------------------------------------------------------------------------------------------------------

sys.path.append('.')

import TimeToolBox.Time

#-------------------------------------------------------------------------------------------------------------------------------


class Information(TimeToolBox.Time.SimpleEvent.AbstractInformation):


    def __init__(self, name: str) -> None:
        self.name: str = name


    def export(self) -> dict:
        return { 'name' : self.name }


    def __eq__(self, other: "Information") -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return self.name


class SimpleEventTest(unittest.TestCase):


    def setUp(self) -> None:

        self.event: TimeToolBox.Time.SimpleEvent = TimeToolBox.Time.SimpleEvent(
            infos = Information(name='Valorant'),
            begin = datetime.datetime(year=2022, month=1, day=1, hour=7, minute=0),
            duration = datetime.timedelta(hours=3)
        )


    def test_export(self) -> None:
        

        infos: Information = self.event.infos
        print(infos.name, self.event.begin, self.event.duration)

        export: dict = self.event.export()
        print(export)

        # valorant: TimeToolBox.Time.SimpleDuration = \
        #     TimeToolBox.Time.SimpleDuration(duration=self.duration_2)
        
#-------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
