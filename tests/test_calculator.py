"""Offline unit tests for synthetic examples."""

import unittest
from calculator import add, subtract


class CalculatorTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-4, 1), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(7, 0), 7)

    def test_add_both_negative(self):
        self.assertEqual(add(-2, -3), -5)


class SubtractTests(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_positive_result_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-4, -6), 2)
        self.assertEqual(subtract(-4, 1), -5)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(7, 0), 7)
        self.assertEqual(subtract(0, 7), -7)

    def test_subtract_inverse_of_add(self):
        for a, b in [(2, 3), (-4, 1), (0, 9), (-5, -5)]:
            self.assertEqual(subtract(add(a, b), b), a)


if __name__ == "__main__":
    unittest.main()
