import unittest

from pythonProjects.Tests.addce import add_ce


class TestAddCe(unittest.TestCase):

    def test_even_length(self):
        self.assertEqual(add_ce('helloo'), 'hellooce')

    def test_odd_length(self):
        self.assertEqual(add_ce('hello'), 'helceclo')

    def test_short_word(self):
        self.assertEqual(add_ce('joy'), 'joyce')

    def test_single_character(self):
        self.assertEqual(add_ce('a'), 'ace')

    def test_empty_string(self):
        self.assertEqual(add_ce(''), 'ce')
