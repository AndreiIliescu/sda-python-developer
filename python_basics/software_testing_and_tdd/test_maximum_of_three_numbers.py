import unittest
from maximum_of_three_numbers import max_of_three


class TestMaximumOfThreeNumbers(unittest.TestCase):
    def test_there_are_not_numbers(self):
        expected_results = 'Te rog introdu doar cifre de la tastatura'
        self.assertEqual(expected_results, max_of_three('a', 'b', 'c'))

    def test_there_are_not_positive(self):
        expected_results = 'Numbers is not positives'
        self.assertEqual(expected_results, max_of_three(-1, -3, -2))

    def test_first_number_is_greater_than_second_and_third(self):
        self.assertEqual(5, max_of_three(5, 3, 2))

    def test_second_number_is_greater_than_first_and_third(self):
        self.assertEqual(5, max_of_three(3, 5, 2))

    def test_third_number_is_greater_than_second_and_first(self):
        self.assertEqual(5, max_of_three(2, 3, 5))

    def test_first_number_equal_second_and_greater_than_third(self):
        self.assertEqual(5, max_of_three(5, 5, 2))

    def test_first_number_equal_third_and_greater_than_second(self):
        self.assertEqual(5, max_of_three(5, 3, 5))

    def test_second_number_equal_third_and_greater_than_first(self):
        self.assertEqual(5, max_of_three(3, 5, 5))



    def test_output_not_none(self):
        self.assertIsNotNone(max_of_three(1.2,4,1))

if __name__ == '__main__':
    unittest.main()
