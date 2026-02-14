import unittest
from encrypt import encrypt_message


class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        self.message = "message"
        self.key = 1

    def test_return_something(self):
        self.assertIsNotNone(encrypt_message(self.message, self.key))

    def test_return_is_str(self):
        self.assertIsInstance(encrypt_message(self.message, self.key), str)

    def test_return_length(self):
        self.assertGreater(len(encrypt_message(self.message, self.key)), 0)

    def test_equal_number_of_characters(self):
        self.assertEqual(len(self.message), len(encrypt_message(self.message, self.key)))

    def test_input_different_output(self):
        self.assertNotEqual(self.message, encrypt_message(self.message, self.key))

    def test_key_is_not_int(self):
        expected_results = 'Key is not an integer, type a new integer key.'
        self.assertEqual(expected_results, encrypt_message(self.message, '0'))

    def test_key_equal_0(self):
        expected_results = 'Key can not be 0.'
        self.assertEqual(expected_results, encrypt_message(self.message, 0))

    def test_input_is_not_str(self):
        expected_results = 'Type a string for input.'
        self.assertEqual(expected_results, encrypt_message(45, self.key))

    def test_input_length_is_equal_0(self):
        expected_results = 'The message is empty, type a message.'
        self.assertEqual(expected_results, encrypt_message('', self.key))

    def test_message_is_correct_encrypted(self):
        expected_results = 'def'
        self.assertEqual(expected_results, encrypt_message('abc', 3))

    def test_index_out_of_range(self):
        expected_results = ' ab'
        self.assertEqual(expected_results, encrypt_message('789', 3))

    def test_key_is_greater_then_double_length_of_alphabet(self):
        expected_results = 'abc'
        self.assertEqual(expected_results, encrypt_message('789', 194))

    def test_white_spaces_in_message(self):
        expected_results = 'dec'
        self.assertEqual(expected_results, encrypt_message('ab ', 3))


if __name__ == "__main__":
    unittest.main()
