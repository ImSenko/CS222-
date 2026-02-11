import unittest
from Assignment_5 import fahtocel, fibbonaci

class TestAssignment5(unittest.TestCase):

    def test_fahtocel(self):
        self.assertAlmostEqual(fahtocel(32), 0.0)
        self.assertAlmostEqual(fahtocel(212), 100.0)
        self.assertAlmostEqual(fahtocel(98.6), 37.0)
        self.assertAlmostEqual(fahtocel(0), -17.7778, places=4)

    def test_fibbonaci(self):
        self.assertEqual(fibbonaci(0), [])
        self.assertEqual(fibbonaci(1), [0])
        self.assertEqual(fibbonaci(2), [0, 1])
        self.assertEqual(fibbonaci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibbonaci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()