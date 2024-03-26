import sys
sys.path.append('../tasks/')

from eleven_inside_str import *
import unittest

class TestIsSubsequence(unittest.TestCase):
    def test_example(self):
        self.assertTrue(is_subsequence("uio", "quefio"))

    def test_not_subsequence(self):
        self.assertFalse(is_subsequence("uio", "qefo"))

    def test_empty_a(self):
        self.assertTrue(is_subsequence("", "quefio"))

    def test_empty_b(self):
        self.assertFalse(is_subsequence("uio", ""))

    def test_both_empty(self):
        self.assertTrue(is_subsequence("", ""))

    def test_same_strings(self):
        self.assertTrue(is_subsequence("uio", "uio"))

if __name__ == '__main__':
    unittest.main()
