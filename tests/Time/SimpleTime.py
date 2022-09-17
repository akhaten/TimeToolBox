#-------------------------------------------------------------------------------------------------------------------------------

import unittest
import sys
import datetime

#-------------------------------------------------------------------------------------------------------------------------------

sys.path.append('.')

import TimeToolBox.Time



#-------------------------------------------------------------------------------------------------------------------------------

class SimpleTimeTest(unittest.TestCase):

    def setUp(self) -> None:

        self.begin: datetime.datetime = datetime.datetime(year=2022, month=1, day=1, hour=7, minute=0)
        self.duration: datetime.timedelta = datetime.timedelta(hours=1)
        self.time:TimeToolBox.Time.SimpleTime = TimeToolBox.Time.SimpleTime(self.begin, self.duration)



        
    def test_export(self) -> None:
        

        print(self.time.begin, self.time.duration)

        # valorant: TimeToolBox.Time.SimpleDuration = \
        #     TimeToolBox.Time.SimpleDuration(duration=self.duration_2)
        
#-------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
