import sys
sys.path.append('../tasks/')

from two_part_swap import *
import unittest

class TestRotateArray(unittest.TestCase):
    def test_example(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])

    def test_full_rotation(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_rotation_larger_than_length(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5], 8), [3, 4, 5, 1, 2])

    def test_empty_array(self):
        self.assertEqual(rotate_array([], 3), [])

    def test_single_element(self):
        self.assertEqual(rotate_array([1], 0), [1])

if __name__ == '__main__':
    unittest.main()
