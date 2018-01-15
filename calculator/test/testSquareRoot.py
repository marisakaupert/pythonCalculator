import unittest


class SquareRootTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_getting_square_root_of_number(self):
        result = self.test.squareRoot(144)
        self.assertEqual(12, result)

    def test_getting_square_root_of_zero(self):
        result = self.test.squareRoot(0)
        self.assertEqual(0, result)

    def test_getting_square_root_of_negative_number(self):
        result = self.test.squareRoot(-144)
        self.assertEqual("Invalid Input", result)

    def test_getting_square_root_of_invalid_number(self):
        result = self.test.squareRoot(None)
        self.assertEqual("Invalid Input", result)


if __name__ == '__main__':
    unittest.main()