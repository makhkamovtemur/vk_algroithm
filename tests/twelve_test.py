import sys
sys.path.append('../tasks/')

from twelve_find_square import *
import unittest

class TestSquareRoot(unittest.TestCase):
    def test_small_number(self):
        self.assertEqual(square_root(3), 1)

    def test_perfect_square(self):
        self.assertEqual(square_root(16), 4)

    def test_large_number(self):
        self.assertEqual(square_root(300), 17)

    def test_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_one(self):
        self.assertEqual(square_root(1), 1)

if __name__ == '__main__':
    unittest.main()
