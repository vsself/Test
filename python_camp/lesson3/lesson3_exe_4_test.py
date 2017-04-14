import unittest
import lesson3_exe_4

class TestRemoveDuplicate(unittest.TestCase):
	def test_remove_duplicate(self):
		result=lesson3_exe_4.remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])
		self.assertEqual(str(result.sort()),str([[10, 20], [30, 56, 25], [33], [40]].sort()))	
