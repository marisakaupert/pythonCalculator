import unittest
from main import MainFunctions


class SubtractionTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_subtracting_two_numbers(self):
        result = self.test.subtract(6, 3)
        self.assertEqual(3, result)

    def test_subtracting_three_numbers(self):
        result = self.test.subtract(10, 3, 4)
        self.assertEqual(3, result)

    def test_subtracting_negative_numbers(self):
        result = self.test.subtract(-10, 6, 4)
        self.assertEqual(-20, result)

    def test_subtracting_multiple_numbers(self):
        result = self.test.subtract(-10, 10, 10, 10, 5)
        self.assertEqual(-45, result)

if __name__ == '__main__':
    unittest.main()