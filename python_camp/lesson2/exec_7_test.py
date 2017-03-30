import unittest
import exec_7

class TestCaculator(unittest.TestCase):
    def test_caculator_case_1(self):
        result = exec_1.calculator('3+2-4')
        self.assertEqual(result, 1)
    def test_caculator_case_1(self):
        result = exec_1.calculator('3+2*4')
        self.assertEqual(result, 11)
    def test_caculator_case_1(self):
        result = exec_1.calculator('(3+2)*4')
        self.assertEqual(result, 20)
    def test_caculator_case_1(self):
        result = exec_1.calculator('(3+2)/5')
        self.assertEqual(result, 1)
