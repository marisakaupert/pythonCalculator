import unittest
from arithmaticFunctions import MainFunctions


class AdditionTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_adding_two_numbers(self):
        result = self.test.add(5, 3)
        self.assertEqual(8, result)

    def test_adding_multiple_numbers(self):
        result = self.test.add(5, 3, 10)
        self.assertEqual(18, result)

    def test_adding_negative_numbers(self):
        result = self.test.add(-10, 5, -10)
        self.assertEqual(-15, result)

    def test_adding_no_numbers(self):
        result = self.test.add()
        self.assertEqual(0, result)

    def test_adding_decimal_numbers(self):
        result = self.test.add(2.5, 3.75)
        self.assertEqual(6.25, result)


if __name__ == '__main__':
    unittest.main()