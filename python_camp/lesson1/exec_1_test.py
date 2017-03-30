import unittest
import exec_1


class TestCaculator(unittest.TestCase):
    def test_caculator_case_1(self):
        result = exec_1.caculator(1, 2, '+')
        self.assertEqual(result, 3)