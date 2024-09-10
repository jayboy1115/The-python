import unittest

from Tests.equalstrings import equal_strings


class TestEqualStrings(unittest.TestCase):
    def test_equal_strings(self):
        self.assertTrue(equal_strings("love", "evol"))
        self.assertTrue(equal_strings("hello", "hello"))
        self.assertFalse(equal_strings("hello", "world"))



