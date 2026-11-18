"""Offline unit tests for synthetic examples."""

import unittest
from calculator import add, multiply


class CalculatorTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-4, 1), -3)

    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(3, -4), -12)
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 7), 0)
        self.assertEqual(multiply(-7, 0), 0)
        self.assertEqual(multiply(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
