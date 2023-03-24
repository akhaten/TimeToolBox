#-------------------------------------------------------------------------------------------------------------------------------

import unittest
import sys
import datetime

#-------------------------------------------------------------------------------------------------------------------------------

sys.path.append('.')



import TimeToolBox.Assertion.Datetime

from TimeToolBox.Time import SimpleTime



#-------------------------------------------------------------------------------------------------------------------------------

class AssertionSimpleTimeTest(unittest.TestCase):


    def setUp(self) -> None:

        self.begin_1: datetime.datetime = datetime.datetime(year=2022, month=1, day=1, hour=7, minute=0)
        self.duration_1: datetime.timedelta = datetime.timedelta(minutes=30)

        self.begin_2: datetime.datetime = datetime.datetime(year=2022, month=1, day=2, hour=7, minute=0)
        self.duration_2: datetime.timedelta = datetime.timedelta(hours=1)


    def test_begin_before_datetime(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.datetime = self.begin_1-datetime.timedelta(minutes=1)
        after: datetime.datetime = self.begin_1+datetime.timedelta(minutes=1)

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.begin_before(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not begin before datetime'
        )

        # -------------------------------------------------------


        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.begin_before(
                valorant, after),
            second=True,
            msg = 'Valorant shoud begin before datetime'
        )


    def test_begin_after_datetime(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.datetime = self.begin_1-datetime.timedelta(minutes=1)
        after: datetime.datetime = self.begin_1+datetime.timedelta(minutes=1)

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.begin_after(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not begin after datetime'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.begin_after(
                valorant, before),
            second=True,
            msg = 'Valorant shoud begin after datetime'
        )


    def test_finish_before_datetime(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.datetime = valorant.end-datetime.timedelta(minutes=1)
        after: datetime.datetime = valorant.end+datetime.timedelta(minutes=1)

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.finish_before(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not finish before datetime'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.finish_before(
                valorant, after),
            second=True,
            msg = 'Valorant shoud finish before datetime'
        )


    def test_finish_after_datetime(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.datetime = valorant.end-datetime.timedelta(minutes=1)
        after: datetime.datetime = valorant.end+datetime.timedelta(minutes=1)

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.finish_after(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not finish after datetime'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.finish_after(
                valorant, before),
            second=True,
            msg = 'Valorant shoud finish after datetime'
        )
   

    def test_between_datetime(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        begin_before: datetime.datetime = valorant.begin-datetime.timedelta(minutes=1)
        begin_after: datetime.datetime = valorant.begin+datetime.timedelta(minutes=1)
        end_before: datetime.datetime = valorant.end-datetime.timedelta(minutes=1)
        end_after: datetime.datetime = valorant.end+datetime.timedelta(minutes=1)

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.between(
                valorant, begin_before, end_before),
            second=False,
            msg = 'Valorant shoud not be between datetimes'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.between(
                valorant, begin_after, end_before),
            second=False,
            msg = 'Valorant shoud not be between datetimes'
        )

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.between(
                valorant, begin_after, end_after),
            second=False,
            msg = 'Valorant shoud not be between datetimes'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.Datetime.between(
                valorant, begin_before, end_after),
            second=True,
            msg = 'Valorant shoud be between datetimes'
        )


    def test_begin_before_date(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.date = (valorant.begin-datetime.timedelta(days=1)).date()
        after: datetime.date = (valorant.begin+datetime.timedelta(days=1)).date()

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.begin_before_date(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not begin before date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.begin_before_date(
                valorant, after),
            second=True,
            msg = 'Valorant shoud begin before date'
        )


    def test_begin_after_date(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.date = (valorant.begin-datetime.timedelta(days=1)).date()
        after: datetime.date = (valorant.begin+datetime.timedelta(days=1)).date()

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.begin_after_date(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not begin after date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.begin_after_date(
                valorant, before),
            second=True,
            msg = 'Valorant shoud begin after date'
        )


    def test_finish_before_date(self):
        
        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.date = (valorant.begin-datetime.timedelta(days=1)).date()
        after: datetime.date = (valorant.begin+datetime.timedelta(days=1)).date()

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_before_date(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not finish before date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_before_date(
                valorant, after),
            second=True,
            msg = 'Valorant shoud be finish before date'
        )


    def test_finish_after_date(self):
        
        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.date = (valorant.begin-datetime.timedelta(days=1)).date()
        after: datetime.date = (valorant.begin+datetime.timedelta(days=1)).date()

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_after_date(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not finish after date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_after_date(
                valorant, before),
            second=True,
            msg = 'Valorant shoud be finish after date'
        )


    def test_between_date(self):
        
        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before_1: datetime.date = (valorant.begin-datetime.timedelta(days=2)).date()
        before_2: datetime.date = (valorant.begin-datetime.timedelta(days=1)).date()
        date: datetime.date = valorant.begin.date()
        after_1: datetime.date = (valorant.end+datetime.timedelta(days=1)).date()
        after_2: datetime.date = (valorant.end+datetime.timedelta(days=1)).date()

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, before_1, before_2),
            second=False,
            msg = 'Valorant shoud not be between date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, after_1, after_2),
            second=False,
            msg = 'Valorant shoud not be between date'
        )

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, before_2, after_1),
            second=True,
            msg = 'Valorant shoud be between date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, date, after_1),
            second=True,
            msg = 'Valorant shoud be between date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, before_1, date),
            second=True,
            msg = 'Valorant shoud be between date'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_date(
                valorant, date, date),
            second=True,
            msg = 'Valorant shoud be between date'
        )


    def test_begin_after_time(self):
        
        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.time = (valorant.begin-datetime.timedelta(hours=1)).time()
        after: datetime.time = (valorant.begin+datetime.timedelta(hours=1)).time()

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.begin_after_time(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not begin after time'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.begin_after_time(
                valorant, before),
            second=True,
            msg = 'Valorant shoud begin after time'
        )


    def test_begin_before_time(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.time = (valorant.begin-datetime.timedelta(hours=1)).time()
        after: datetime.time = (valorant.begin+datetime.timedelta(hours=1)).time()

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.begin_before_time(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not begin before time'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.begin_before_time(
                valorant, after),
            second=True,
            msg = 'Valorant shoud begin before time'
        )


    def test_finish_after_time(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.time = (valorant.end-datetime.timedelta(hours=1)).time()
        after: datetime.time = (valorant.end+datetime.timedelta(hours=1)).time()
        
        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.finish_after_time(
                valorant, after),
            second=False,
            msg = 'Valorant shoud not finish after time'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_after_time(
                valorant, before),
            second=True,
            msg = 'Valorant shoud finsh after time'
        )


    def test_finish_before_time(self):

        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )

        before: datetime.time = (valorant.end-datetime.timedelta(hours=1)).time()
        after: datetime.time = (valorant.end+datetime.timedelta(hours=1)).time()
        
        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.finish_before_time(
                valorant, before),
            second=False,
            msg = 'Valorant shoud not finish before time'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.finish_before_time(
                valorant, after),
            second=True,
            msg = 'Valorant shoud finsh before time'
        )


    def test_between_time(self):
        
        # -------------------------------------------------------

        valorant: SimpleTime = SimpleTime(
            begin = self.begin_1, duration=self.duration_1
        )


        before_1: datetime.time = (valorant.begin-datetime.timedelta(hours=2)).time()
        before_2: datetime.time = (valorant.begin-datetime.timedelta(hours=1)).time()
        time: datetime.time = valorant.begin.time()
        after_1: datetime.time = (valorant.end+datetime.timedelta(hours=1)).time()
        after_2: datetime.time = (valorant.end+datetime.timedelta(hours=1)).time()

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, before_1, before_2),
            second=False,
            msg = 'Valorant shoud not be between times'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, after_1, after_2),
            second=False,
            msg = 'Valorant shoud not be between times'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, before_1, time),
            second=False,
            msg = 'Valorant shoud not be between times'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, time, time),
            second=False,
            msg = 'Valorant shoud not be between times'
        )

        # -------------------------------------------------------
        
        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, before_2, after_1),
            second=True,
            msg = 'Valorant shoud be between times'
        )

        # -------------------------------------------------------

        self.assertEqual(
            first=TimeToolBox.Assertion.between_time(
                valorant, time, after_1),
            second=True,
            msg = 'Valorant shoud be between times'
        )


    def test_in_only_a_day(self):
        pass


#-------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
