from unittest import TestCase

from multiples import multiplesofthree


class TestKeyCube(TestCase):
    def test_that_johnson_function_exist(self):
        multiplesofthree.get_key_cube = [1, 2, 3, 4, 5]

    def test_that_get_cube_function_return_dict(self):
        actual = multiplesofthree.get_key_cube([1, 2, 3, 4, 5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)


