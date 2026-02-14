import unittest
from password_validation import validate_password


class TestPassword(unittest.TestCase):
    def setUp(self):
        self.password = "123345678"

    def test_return_is_not_none(self):
        self.assertIsNotNone(validate_password(self.password))

    def test_return_is_boolean(self):
        self.assertIsInstance(validate_password(self.password), bool)

    def test_input_is_not_string(self):
        expected = "Password is not string!"
        self.assertEqual(expected, validate_password(123))

    def test_less_than_minimum_password_length(self):
        expected = "Minimum 8 characters"
        self.assertEqual(expected, validate_password('1234567'))

    def test_greater_than_maximum_password_len(self):
        expected = "Maximum 16 characters"
        self.assertEqual(expected, validate_password('12345678901234567'))

    def test_password_not_include_upper(self):
        self.assertFalse(validate_password('abc1234@!'))

    def test_password_not_include_lower(self):
        self.assertFalse(validate_password('ABC1234@!'))

    def test_password_not_include_digit(self):
        self.assertFalse(validate_password('ABCaaaa@!'))

    def test_password_not_include_symbol(self):
        self.assertFalse(validate_password('ABCaaaa445'))

    def test_password_is_valid(self):
        self.assertTrue(validate_password('ABCaaaa#$445'))


if __name__ == '__main__':
    unittest.main()
