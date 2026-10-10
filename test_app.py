import unittest
from app import add, mod, pwr, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)
    def test_modulus(self):
        self.assertEqual(mod(10, 3), 1)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            mod(10, 0)

    def test_power(self):
        self.assertEqual(pwr(2, 3), 8)

if __name__ == "__main__":
    unittest.main()