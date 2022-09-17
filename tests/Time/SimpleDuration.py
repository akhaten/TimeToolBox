#-------------------------------------------------------------------------------------------------------------------------------

import unittest
import sys
import datetime

#-------------------------------------------------------------------------------------------------------------------------------

sys.path.append('.')

import TimeToolBox.Time



#-------------------------------------------------------------------------------------------------------------------------------

class SimpleDurationTest(unittest.TestCase):

    def setUp(self) -> None:

        self.valorant: TimeToolBox.Time.SimpleDuration = \
            TimeToolBox.Time.SimpleDuration(
                duration=datetime.timedelta(hours=1)
            )

        
    def test_export(self) -> None:
        
        export: dict = self.valorant.export()
        print(export)
        

        # valorant: TimeToolBox.Time.SimpleDuration = \
        #     TimeToolBox.Time.SimpleDuration(duration=self.duration_2)

#-------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
