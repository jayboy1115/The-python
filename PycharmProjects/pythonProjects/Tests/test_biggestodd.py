import unittest
import biggest_odd
from Tests import biggestodd


class TestBigOdd(unittest.TestCase):

    def test_that_biggest_odd_function_exists(self):
        biggestodd.biggest_odd("23956")

    def test_that_biggest_function_returns_biggest_odd(self):
        result = biggestodd.biggest_odd("23956")
        self.assertEqual(result, 9)