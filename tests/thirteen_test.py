import sys
sys.path.append('../tasks/')

from thirteen_palindrom import *
import unittest

class TestPalindromeMethods(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome_stack("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome_two_pointers("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome_stack("race a car"))
        self.assertFalse(is_palindrome_two_pointers("race a car"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome_stack(""))
        self.assertTrue(is_palindrome_two_pointers(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome_stack("a"))
        self.assertTrue(is_palindrome_two_pointers("a"))

if __name__ == '__main__':
    unittest.main()
