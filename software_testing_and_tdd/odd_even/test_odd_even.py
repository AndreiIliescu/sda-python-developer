import unittest
from odd_even import odd_even

class OddEvenTest(unittest.TestCase):
    # is not none - returneaza ceva
    def test_is_not_none(self):
        self.assertIsNotNone(odd_even(1))

    # return type
    def test_return_string(self):
        self.assertIsInstance(odd_even(5), str)

    # input type invalid - altceva decat int
    def test_input_type_invalid(self):
        expected = 'Error - number must be integer!'
        self.assertEqual(expected, odd_even('5'))

    # returnare mesaj pt par
    def test_number_is_even(self):
        expected = 'The number is even!'
        self.assertEqual(expected, odd_even(2))

    # returnare mesaj pt impar
    def test_number_is_odd(self):
        expected = 'The number is odd!'
        self.assertEqual(expected, odd_even(5))


if __name__ == '__main__':
    unittest.main()
