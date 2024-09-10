import unittest

from Tests.arrangestring import swap_first_two_chars


class TestSwapFirstTwoChars(unittest.TestCase):

    def test_function_exists(self):
        self.assertTrue('swap_first_two_chars' in globals())

    def test_swap_first_two_chars(self):
        self.assertEqual(swap_first_two_chars('abc', 'xyz'), 'bac yxz')

    def test_swap_first_two_chars_with_single_char_strings(self):
        self.assertEqual(swap_first_two_chars('a', 'b'), 'a b')

    def test_swap_first_two_chars_with_empty_strings(self):
        self.assertEqual(swap_first_two_chars('', ''), ' ')


