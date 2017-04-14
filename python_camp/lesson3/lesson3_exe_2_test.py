import unittest
import lesson3_exe_2

class TestChangeChar(unittest.TestCase):
	def test_test_uniq_chars_1(self):
		result=lesson3_exe_2.change_char('abcaa')
		self.assertEqual(result,'abc$$')
  		
	def test_test_uniq_chars_2(self):
		result=lesson3_exe_2.change_char('kobacko')
		self.assertEqual(result,'kobac$o')
  		
	def test_test_uniq_chars_3(self):
		result=lesson3_exe_2.change_char('$54$12')
		self.assertEqual(result,'$54$12')
