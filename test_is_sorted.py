from unittest import TestCase
import sorted


class TestIsSorted(TestCase):

    def test_is_sorted_positive_sorted(self):
        actual_value = sorted.is_sorted([3, 4, 5])
        expected_value = True
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_negative_unsorted(self):
        actual_value = sorted.is_sorted([-5, -6, -3])
        expected_value = False
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_positive_and_negative_unsorted(self):
        actual_value = sorted.is_sorted([-5, 5, -3])
        expected_value = False
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_positive_and_negative_sorted(self):
        actual_value = sorted.is_sorted([-5, -4, 3])
        expected_value = True
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_empty_list(self):
        actual_value = sorted.is_sorted([])
        expected_value = True
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_one_element_list(self):
        actual_value = sorted.is_sorted([1])
        expected_value = True
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_is_sorted_several_elements_list(self):
        actual_value = sorted.is_sorted([-5, -4, 3, 6, -9])
        expected_value = False
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)
