from unittest import TestCase
import sorted

class TestIsSorted(TestCase):
    def test_is_sorted_zero(self):
        actualValue = sorted.is_sorted([0, 0, 0])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_positive_sorted(self):
        actualValue = sorted.is_sorted([3, 4, 5])
        expectedValue = True
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_positive_unsorted(self):
        actualValue = sorted.is_sorted([5, 1, 3])
        expectedValue = False
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_is_sorted_negative_unsorted(self):
        actualValue = sorted.is_sorted([-5, -6, -3])
        expectedValue = False
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)
