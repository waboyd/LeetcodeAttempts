import unittest
from reversestring344 import Solution

class TestReversestring(unittest.TestCase):
    """ Tests the method Solution.reverseString in
        the file reversestring344.py."""
    def setUp(self):
        """ Create an object of the Solution class"""
        self.test_a = Solution()
    def test_basic(self):
        """ Basic test of this unittest class."""
        x = 5
        self.assertEqual(5, x)
        return
    def test_empty_string(self):
        """ Test for empty string input. """
        result = self.test_a.reverseString("")
        self.assertEqual("", result)
        return
    def test_single_character(self):
        """ Test for empty string input. """
        result = self.test_a.reverseString("a")
        self.assertEqual("a", result)
        return
    def test_two_characters(self):
        """ Test for a two-character input. """
        result = self.test_a.reverseString("xy")
        self.assertEqual("yx", result)
        return
    def test_five_characters(self):
        """ Test for a five-character input. """
        result = self.test_a.reverseString("aeiou")
        self.assertEqual("uoiea", result)
        return

if __name__ == "__main__":
    unittest.main()
