import unittest
from Tests.charcounter import CharCounter, char_counter


class TestCharCounter(unittest.TestCase):

    def test_char_counter(self):
        self.assertEqual(char_counter('tree'), {'t': 1, 'r': 1, 'e': 2})
        self.assertEqual(char_counter('hello'), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(char_counter('abcde'), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
        self.assertEqual(char_counter(''), {})

    def test_char_counter_with_spaces(self):
        self.assertEqual(char_counter('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_char_counter_with_number_input(self):
        with self.assertRaises(ValueError):
            char_counter('hello123')

    def test_char_counter_with_number_mixed_with_char_input(self):
        with self.assertRaises(ValueError):
            char_counter('hello123')

    def test_char_counter_with_special_characters(self):
        self.assertEqual(char_counter('semicolon.africa'), {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1})







