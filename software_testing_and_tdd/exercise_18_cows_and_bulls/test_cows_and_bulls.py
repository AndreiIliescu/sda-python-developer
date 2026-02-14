import unittest
from Cows_and_Bulls import cows_and_bulls


class TestCowAndBulls(unittest.TestCase):
    def test_return_something(self):
        self.assertIsNotNone(cows_and_bulls(2367, 1234, 3))

    def test_return_type(self):
        self.assertIsInstance(cows_and_bulls(2367, 1234, 3), str)

    def test_return_length_min(self):
        self.assertGreater(len(cows_and_bulls(2367, 1234, 3)), 8)

    def test_input_type_chances_is_not_int(self):
        expected_result = 'Error: the chances parameter must be int'
        self.assertEqual(expected_result, cows_and_bulls(2367, 1234, '3'))

    def test_input_greater_chances_that(self):
        expected_result = 'Error: the chances must be greater than 0'
        self.assertEqual(expected_result, cows_and_bulls(2367, 1234, 0))

    def test_input_less_chances_that(self):
        expected_result = 'Error: the chances must be less than 10'
        self.assertEqual(expected_result, cows_and_bulls(2367, 1234, 11))

    def test_input_guess_is_not_str_type(self):
        expected_result = 'Error: the guess is not a valid type '
        self.assertEqual(expected_result,cows_and_bulls(2367, 1234, 3))

    def test_input_guess_length_is_not_4(self):
        expected_result = 'Error: only 4 characters'
        self.assertEqual(expected_result,cows_and_bulls(2367, '12345', 3))

    def test_input_guess_is_not_only_digits(self):
        expected_result = 'Error guess must contain only digits'
        self.assertEqual(expected_result, cows_and_bulls(2356,'1 3@',3))

    def test_input_generated_number_is_not_str_type(self):
        expected_result = 'Error: the generated_number is not a valid type '
        self.assertEqual(expected_result,cows_and_bulls(2367, '1234', 3))

    def test_input_generated_number_length_is_not_4(self):
        expected_result = 'Error: only 4 characters'
        self.assertEqual(expected_result,cows_and_bulls('23867', '1234', 3))

    def test_input_generated_number_is_not_only_digits(self):
        expected_result = 'Error generated_number must contain only digits'
        self.assertEqual(expected_result, cows_and_bulls('12 #','1234',3))



if __name__ == '__main__':
    unittest.main()
