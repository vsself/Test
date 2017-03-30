import unittest
import exec_5

class TestFactorial(unittest.TestCase):
    def test_factorial_case_1(self):
        result = exec_5.factorial(5)
        self.assertEqual(result, 120)
