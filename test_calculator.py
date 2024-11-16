import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, 5), 8)
        # Add the following test methods to the TestCalculator class:
    def test_subbtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(5, 3), 2)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(6, 2), 3)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2, 1), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)
if __name__ == '__main__':
    unittest.main()