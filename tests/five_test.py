import sys
sys.path.append('../tasks/')

from five_zeros_back import *
import unittest

class TestMoveZerosToEnd(unittest.TestCase):
    def test_example(self):
        self.assertEqual(move_zeros_to_end([5, 0, 2, 3, 0, 1, 0]), [5, 2, 3, 1, 0, 0, 0])

    def test_all_zeros(self):
        self.assertEqual(move_zeros_to_end([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_no_zeros(self):
        self.assertEqual(move_zeros_to_end([0, 1, 2, 3, 4, 0]), [1, 2, 3, 4, 0, 0])

    def test_empty_array(self):
        self.assertEqual(move_zeros_to_end([]), [])

    def test_one_zero(self):
        self.assertEqual(move_zeros_to_end([0]), [0])

    def test_one_non_zero(self):
        self.assertEqual(move_zeros_to_end([1]), [1])

if __name__ == '__main__':
    unittest.main()
