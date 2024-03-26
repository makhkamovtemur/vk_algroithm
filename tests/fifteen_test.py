import sys
sys.path.append('../tasks/')

from fifteen_del_dublicate import *
import unittest

class TestRemoveAdjacentDuplicates(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(remove_adjacent_duplicates("cdffd"), "c")

    def test_example_2(self):
        self.assertEqual(remove_adjacent_duplicates("uioouiouuo"), "uiui")

    def test_empty_string(self):
        self.assertEqual(remove_adjacent_duplicates(""), "")

    def test_no_duplicates(self):
        self.assertEqual(remove_adjacent_duplicates("abc"), "abc")

    def test_all_duplicates(self):
        self.assertEqual(remove_adjacent_duplicates("aabbcc"), "")

if __name__ == '__main__':
    unittest.main()
