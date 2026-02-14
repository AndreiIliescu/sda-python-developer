import unittest
from list_overlap import list_common_elements


class TestListCommonElements(unittest.TestCase):

    def test_return_is_not_none(self):
        self.assertIsNotNone(list_common_elements([7], [1]))

    def test_return_type_list(self):
        self.assertIsInstance(list_common_elements([2], [2]), list)

    def test_retun_len_is_greater_than_zero(self):
        self.assertGreater(len(list_common_elements([8], [6])), 0)

    def test_parameter_1_is_not_list(self):
        expected_result = "This first parameter must be a list"
        self.assertEqual(expected_result, list_common_elements(9, [5]))

    def test_parameter_2_is_not_list(self):
        expected_result = "This second parameter must be a list"
        self.assertEqual(expected_result, list_common_elements([9], "abc"))

    def test_first_list_is_empty(self):
        expected_result = "The fist list can not be empty"
        self.assertEqual(expected_result, list_common_elements([], [1, 2, 3]))

    def test_second_list_is_empty(self):
        expected_result = "The second list can not be empty"
        self.assertEqual(expected_result, list_common_elements([4, 5, 6], []))

    def test_when_no_common_elements(self):
        expected_result = "There are no common elements in both lists"
        self.assertEqual(expected_result, list_common_elements([1, 2, 3], [4, 5, 6]))

    def test_when_are_common_elements(self):
        self.assertEqual([2, 3], list_common_elements([1, 2, 3], [2, 3, 4]))

    def test_when_are_duplicate_elements(self):
        self.assertEqual([2, 3], list_common_elements([1, 2, 3, 2, 8, 3], [2, 3, 4, 3, 3, 2, 9]))


if __name__ == "__main__":
    unittest.main()
