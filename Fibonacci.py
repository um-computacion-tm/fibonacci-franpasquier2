import unittest

from FIbonacci_2 import fibonacci 

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci(1))
    def test_2(self):
        self.assertEqual(1, fibonacci(2))
    def test_3(self):
        self.assertEqual(2, fibonacci(3))
    def test_4(self):
        self.assertEqual(3, fibonacci(4))

if __name__ == '__main__':
    unittest.main()