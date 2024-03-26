import sys
sys.path.append('../tasks/')

from four_even_forward import *
import unittest

class TestMoveEvensForward(unittest.TestCase):
    def test_example(self):
        self.assertEqual(move_evens_forward([3, 2, 4, 1, 11, 8, 9]), [2, 4, 8, 1, 11, 3, 9])

    def test_all_evens(self):
        self.assertEqual(move_evens_forward([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odds(self):
        self.assertEqual(move_evens_forward([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_empty_array(self):
        self.assertEqual(move_evens_forward([]), [])

    def test_one_element_even(self):
        self.assertEqual(move_evens_forward([2]), [2])

    def test_one_element_odd(self):
        self.assertEqual(move_evens_forward([1]), [1])

if __name__ == '__main__':
    unittest.main()
