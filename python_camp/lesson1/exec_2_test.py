import unittest
import exec_2


class TestNumberSort(unittest.TestCase):
    def test_number_sort_case_1(self):
        result = exec_2.number_sort([1])
        self.assertEqual(result, [1])

    def test_number_sort_case_2(self):
        result = exec_2.number_sort([4, 1, 8, 6, 3])
        self.assertEqual(result, [1, 3, 4, 6, 8])