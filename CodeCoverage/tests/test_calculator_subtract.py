import unittest
from calculator.calculator import Calculator

class TestCalculatorSubtract(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(Calculator.subtract(-8, -3), -5)

    def test_subtract_positive_from_negative(self):
        self.assertEqual(Calculator.subtract(-5, 3), -8)

    def test_subtract_negative_from_positive(self):
        self.assertEqual(Calculator.subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(Calculator.subtract(7, 0), 7)
        self.assertEqual(Calculator.subtract(0, 7), -7)

    def test_subtract_from_itself(self):
        self.assertEqual(Calculator.subtract(5, 5), 0)

    def test_subtract_large_numbers(self):
        self.assertEqual(Calculator.subtract(1000000, 999999), 1)

    def test_subtract_floating_point(self):
        self.assertAlmostEqual(Calculator.subtract(5.5, 2.2), 3.3, places=2)

# if __name__ == '__main__':
#     unittest.main()
