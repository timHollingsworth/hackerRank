from is_leap_year import is_leap

import unittest

class LeapYearTest(unittest.TestCase):

    def test_2000_leap_year(self):
        self.assertTrue(is_leap(2000))
        
    def test_1952_leap_year(self):
        self.assertTrue(is_leap(1952))

    def test_1990_not_leap_year(self):
        self.assertFalse(is_leap(1990))

if __name__ == '__main__':
    unittest.main()
