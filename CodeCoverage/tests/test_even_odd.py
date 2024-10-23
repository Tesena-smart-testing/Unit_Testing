import unittest
from even_odd import check_number

class TestCheckNumber(unittest.TestCase):
    def test_positive_even(self):
        print("Running test_positive_even")
        self.assertEqual(check_number(2), "positive even")

    def test_positive_odd(self):
        print("Running test_positive_odd")
        self.assertEqual(check_number(3), "positive odd")

    def test_zero(self):
        print("Running test_zero")
        self.assertEqual(check_number(0), "zero")

    def test_negative_even(self):
        print("Running test_negative_even")
        self.assertEqual(check_number(-2), "negative even")

    def test_negative_odd(self):
        print("Running test_negative_odd")
        self.assertEqual(check_number(-3), "negative odd")        

#if __name__ == "__main__":
#    unittest.main()
