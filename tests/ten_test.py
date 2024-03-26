import sys
sys.path.append('../tasks/')

from ten_copy_time import *
import unittest

class TestMinTimeToCopy(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(min_time_to_copy(4, 1, 1), 3)

    def test_example_2(self):
        self.assertEqual(min_time_to_copy(5, 1, 2), 4)

    def test_different_speeds(self):
        self.assertEqual(min_time_to_copy(5, 1, 10), 5)

    def test_one_copy(self):
        self.assertEqual(min_time_to_copy(1, 5, 7), 5)

if __name__ == '__main__':
    unittest.main()
