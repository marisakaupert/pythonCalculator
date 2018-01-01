import unittest
from main import MainFunctions


class PowerOfTwoTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_square_a_number(self):
        result = self.test.powerOfTwo(12)
        self.assertEqual(144, result)

    def test_square_a_negative_number(self):
        result = self.test.powerOfTwo(-1)
        self.assertEqual(1, result)

    def test_square_zero(self):
        result = self.test.powerOfTwo(0)
        self.assertEqual(0, result)

    def test_square_invalid_number(self):
        result = self.test.powerOfTwo(None)
        self.assertEqual("Invalid Input", result)

if __name__ == '__main__':
    unittest.main()