import unittest

from pythonProjects import password_generator


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = password_generator.generate_password(16)
        self.assertEqual(len(password), 16)

    def test_password_has_uppercase(self):
        password = password_generator.generate_password()
        self.assertTrue(any(c.isupper() for c in password))

    def test_password_has_lowercase(self):
        password = password_generator.generate_password()
        self.assertTrue(any(c.islower() for c in password))

    def test_password_has_digits(self):
        password = password_generator.generate_password()
        self.assertTrue(any(c.isdigit() for c in password))

    def test_password_has_special_character(self):
        password = password_generator.generate_password()
        self.assertTrue(any(c in "!\"#$%&'()*+,-./:;<=>?@[\\" + "]^_`{|}~" for c in password))

    def test_password_is_random(self):
        password1 = password_generator.generate_password()
        password2 = password_generator.generate_password()
        self.assertNotEqual(password1, password2)

    def test_invalid_password_length(self):
        with self.assertRaises(ValueError):
            password_generator.generate_password(-1)

    def test_non_integer_length(self):
        with self.assertRaises(ValueError):
            password_generator.generate_password(length=16.5)



