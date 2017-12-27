import unittest
from main import MainFunctions


class MultiplicationTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_multiplying_two_numbers(self):
        result = self.test.multiply(6, 6)
        self.assertEqual(36, result)

    def test_multiplying_three_numbers(self):
        result = self.test.multiply(10, 10, 2)
        self.assertEqual(200, result)

    def test_multiplying_negative_numbers(self):
        result = self.test.multiply(-1, 1, 5)
        self.assertEqual(-5, result)

    def test_multiplying_multiple_numbers(self):
        result = self.test.multiply(-2, 10, 1, 5, 5)
        self.assertEqual(-500, result)

    def test_multiplying_zeroes(self):
        result = self.test.multiply(0, 0, 5)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()