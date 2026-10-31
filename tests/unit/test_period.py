import unittest
from datetime import time
from freste.model.period import Day, Period

class TestPeriod(unittest.TestCase):

    def setUp(self):
        self.day = Day.MONDAY
        self.day_value = "Monday"
        self.start_time = time(8,00,00)
        self.end_time_1 = time(8,40,00)
        self.end_time_2 = time(9,20,00)
        self.period_1 = Period(day= self.day, start_time=self.start_time, end_time=self.end_time_1)
        self.period_2 = Period(day= self.day, start_time=self.start_time, end_time=self.end_time_2)
        self.period_2_id = self.period_2.id

    def test_object(self):
        self.assertIsInstance(self.period_1, Period)
    
    def test_object_start_time(self):
        self.assertIsInstance(self.period_1.start_time, time)
    
    def test_object_end_time(self):
        self.assertIsInstance(self.period_1.end_time, time)
        
    # def test_object_time_is_valid(self):
    #     self.assertGreater(self.period_1.duration, time(0, 0, 0))

    def test_period_day(self):
        self.assertEqual(self.period_1.day.value, self.day_value)

    def test_id_is_string(self):
        self.assertIsInstance(self.period_1.id, str)

    def test_unique_id(self):
        self.assertNotEqual(self.period_1.id, self.period_2.id)

    def test_id_does_not_change(self):
        self.period_2.start_time = self.end_time_1
        self.assertEqual(self.period_2.id, self.period_2_id)


    # def test_all_school_days(self):
    #     pass

    # def test_invalid_day_type(self):
    #     pass

    def test_valid_time_interval(self):
        self.assertGreater(self.end_time_1, self.start_time)

if __name__ == "__main__":
    unittest.main()