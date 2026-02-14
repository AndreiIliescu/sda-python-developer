import unittest
from hangman_game import hangman_validator


class TestHangmanValidator(unittest.TestCase):

    def test_hangman_validator_return_something(self):
        self.assertIsNotNone(hangman_validator("python"))

    def test_hangman_is_not_string(self):
        expected_result = "The data type must be some text"
        self.assertEqual(expected_result, hangman_validator(0))

    def test_guess_length(self):
        expected_result = "Guessed text can not be empty"
        self.assertEqual(expected_result, hangman_validator(""))

    def test_input_contains_special_characters(self):
        expected_result = "The text can not contain special characters"
        self.assertEqual(expected_result, hangman_validator("@"))

    def test_guess_g(self):
        self.assertTrue(hangman_validator("g"))


if __name__ == '__main__':
    unittest.main()
