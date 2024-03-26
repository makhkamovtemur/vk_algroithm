import sys
sys.path.append('../tasks/')

from three_merge import *
import unittest

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])
        self.assertEqual(merge_sorted_arrays([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([1, 3, 5, 7, 0, 0, 0, 0], 4, [2, 4, 6, 8], 4), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_sorted_arrays([0], 0, [1], 1), [1])
        self.assertEqual(merge_sorted_arrays([2, 0], 1, [1], 1), [1, 2])

if __name__ == '__main__':
    unittest.main()
