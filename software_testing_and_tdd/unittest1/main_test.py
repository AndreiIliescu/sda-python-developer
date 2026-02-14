import unittest
from main import add_three


class AddThreeResult(unittest.TestCase):
    def test_any_arg_is_string(self):
        expected_result=None
        self.assertEqual(expected_result, add_three('1', 'doi', 3))

if __name__ == '__main__':
    unittest.main()
