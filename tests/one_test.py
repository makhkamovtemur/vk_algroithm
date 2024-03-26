import sys
sys.path.append('../tasks/')

from one_full_swap import reverse_array_full
import unittest

class TestReverseArrayInPlace(unittest.TestCase):
    def test_even_number_of_elements(self):
        arr = [1, 2, 3, 4, 5, 6]
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(reverse_array_full(arr), expected)

    def test_odd_number_of_elements(self):
        arr = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(reverse_array_full(arr), expected)

    def test_single_element(self):
        arr = [1]
        expected = [1]
        self.assertEqual(reverse_array_full(arr), expected)

    def test_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(reverse_array_full(arr), expected)

if __name__ == '__main__':
    unittest.main()
