import unittest
from main import MainFunctions


class CubeTests(unittest.TestCase):
    def setUp(self):
        self.test = MainFunctions()

    def test_square_a_number(self):
        result = self.test.cube(12)
        self.assertEqual(1728, result)

    def test_square_a_negative_number(self):
        result = self.test.cube(-1)
        self.assertEqual(-1, result)

    def test_square_zero(self):
        result = self.test.cube(0)
        self.assertEqual(0, result)

    def test_square_invalid_number(self):
        result = self.test.cube(None)
        self.assertEqual("Invalid Input", result)

if __name__ == '__main__':
    unittest.main()