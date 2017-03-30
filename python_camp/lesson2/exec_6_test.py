import unittest
import exec_6


class TestCaculator(unittest.TestCase):
    def test_caculator_case_1(self):
        result = exec_6.calculator('+', 10, 1, 5)
        self.assertEqual(result, 16)
    def test_caculator_case_2(self):
        result = exec_6.calculator('-', 10, 1, 5)
        self.assertEqual(result, 4)
    def test_caculator_case_3(self):
        result = exec_6.calculator('-', 10, 5)
        self.assertEqual(result, 5)
    def test_caculator_case_4(self):
        result = exec_6.calculator('*', 10, 5, 2)
        self.assertEqual(result, 100)
    def test_caculator_case_5(self):
        result = exec_6.calculator('/', 10, 5)
        self.assertEqual(result, 2)
