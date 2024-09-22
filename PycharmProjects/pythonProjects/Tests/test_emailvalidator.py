import unittest

from emailvalidator import validate_email


class TestValidateEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("test.name@example.co.uk"))
        self.assertTrue(validate_email("test_name@example.org"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("invalid_email"))
        self.assertFalse(validate_email("test@"))
        self.assertFalse(validate_email("test@example"))
        self.assertFalse(validate_email("@(link unavailable)"))
        self.assertFalse(validate_email("test@(link unavailable)"))
