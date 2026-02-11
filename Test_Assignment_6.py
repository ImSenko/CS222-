import unittest
from Assignment_6 import add, subtract, multiply, divide

class TesstAssignment6(unittest.TestCase):

    def test_calc_a(self):
        self.assertEqual(add(123,231),354)
        
    def test_calc_b(self):
        self.assertEqual(subtract(456,123),333)

    def test_calc_c(self):
        self.assertEqual(multiply(12,12),144)
    
    def test_calc_d(self):
        self.assertEqual(divide(144,12),12)

    def test_fail(self):
        self.assertEqual(divide(12,0),0)  # This test is designed to fail

if __name__ == '__main__':
    unittest.main()