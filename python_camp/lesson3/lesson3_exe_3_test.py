import unittest
import lesson3_exe_3

class TestSortListLast(unittest.TestCase):
	def test_sort_list_last_two(self):
		result=lesson3_exe_3.sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
		self.assertEqual(str(result),str([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]))
 
	def test_sort_list_last_three(self):
		result=lesson3_exe_3.sort_list_last([(2,4,5), (1,5,2), (4,0,3), (2,7, 3), (2,1,1)])
		self.assertEqual(str(result),str([(2, 1, 1), (1, 5, 2), (4, 0, 3),(2, 7, 3),(2, 4, 5)]))
