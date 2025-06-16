import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,4),6)
        self.assertEqual(self.calc.subtract(4,6),-2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,4),40)
        self.assertEqual(self.calc.multiply(-2,6),-12)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,3),2)
        self.assertEqual(self.calc.divide(7,3),2.33,places = 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5,0)

if __name__ == "__main__":
    unittest.main()
