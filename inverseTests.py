import unittest
from main import MainFunctions


class InverseTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_inverse_a_number(self):
        result = self.test.inverse(2)
        self.assertEqual(0.5, result)

    def test_inverse_a_number_with_continuous_numbers(self):
        result = self.test.inverse(12)
        self.assertEqual(0.083333333333, result)

    def test_inverse_a_negative_number(self):
        result = self.test.inverse(-2)
        self.assertEqual(-0.5, result)

    def test_inverse_zero(self):
        result = self.test.inverse(0)
        self.assertEqual("Invalid Input", result)

    def test_inverse_of_none(self):
        result = self.test.inverse(None)
        self.assertEqual("Invalid Input", result)

    def test_inverse_of_false(self):
        result = self.test.inverse(False)
        self.assertEqual("Invalid Input", result)


if __name__ == '__main__':
    unittest.main()