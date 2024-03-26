import sys
sys.path.append('../tasks/')

from fourteen_inside_str_two_pointers import *
import unittest

class TestIsSubsequence(unittest.TestCase):
    def test_subsequence(self):
        self.assertTrue(is_subsequence("abc", "ahbgdc"))

    def test_not_subsequence(self):
        self.assertFalse(is_subsequence("axc", "ahbgdc"))

    def test_empty_s1(self):
        self.assertTrue(is_subsequence("", "ahbgdc"))

    def test_empty_s2(self):
        self.assertFalse(is_subsequence("abc", ""))

    def test_both_empty(self):
        self.assertTrue(is_subsequence("", ""))

if __name__ == '__main__':
    unittest.main()
