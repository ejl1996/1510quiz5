from unittest import TestCase
import sorted


class TestIsSorted(TestCase):

    def test_is_sorted_positive_sorted(self):
        actualValue = sorted.is_sorted([3, 4, 5])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_negative_unsorted(self):
        actualValue = sorted.is_sorted([-5, -6, -3])
        expectedValue = False
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_positive_and_negative_unsorted(self):
        actualValue = sorted.is_sorted([-5, 5, -3])
        expectedValue = False
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_positive_and_negative_sorted(self):
        actualValue = sorted.is_sorted([-5, -4, 3])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_empty_list(self):
        actualValue = sorted.is_sorted([])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_one_element_list(self):
        actualValue = sorted.is_sorted([1])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_several_elements_list(self):
        actualValue = sorted.is_sorted([-5, -4, 3, 6, -9])
        expectedValue = False
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)
