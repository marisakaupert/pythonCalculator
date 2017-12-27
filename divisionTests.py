import unittest
from main import MainFunctions


class DivisionTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_dividing_two_numbers(self):
        result = self.test.divide(6, 6)
        self.assertEqual(1, result)

    def test_dividing_three_numbers(self):
        result = self.test.divide(56, 7, 2)
        self.assertEqual(4, result)

    def test_dividing_negative_numbers(self):
        result = self.test.divide(-64, 2, 4)
        self.assertEqual(-8, result)

    def test_dividing_multiple_numbers(self):
        result = self.test.divide(-64, 2, 4, -1)
        self.assertEqual(8, result)

    def test_dividing_non_divisible_numbers(self):
        result = self.test.divide(64, 6)
        self.assertEqual(10.666666666667, result)

    def test_dividing_zero_in_numerator(self):
        result = self.test.divide(0, 9)
        self.assertEqual(0, result)

    def test_dividing_by_zero(self):
        result = self.test.divide(20, 0)
        self.assertEqual("Cannot divide by 0", result)

if __name__ == '__main__':
    unittest.main()