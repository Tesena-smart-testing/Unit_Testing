import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(Calculator.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(Calculator.add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(Calculator.add(10, -7), 3)

    def test_add_zero(self):
        self.assertEqual(Calculator.add(5, 0), 5)
        self.assertEqual(Calculator.add(0, 5), 5)

    def test_add_large_numbers(self):
        self.assertEqual(Calculator.add(1000000, 2000000), 3000000)

    def test_add_floating_point(self):
        self.assertAlmostEqual(Calculator.add(3.14, 2.86), 6.00, places=2)

# if __name__ == '__main__':
#     unittest.main()
