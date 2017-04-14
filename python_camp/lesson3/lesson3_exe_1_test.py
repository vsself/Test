import unittest
import lesson3_exe_1

class TestTestUniqChars(unittest.TestCase):
	def test_test_uniq_chars_none(self):
		result=lesson3_exe_1.test_uniq_chars(None)
		self.assertFalse(result)
  		
	def test_test_uniq_chars_null(self):
		result=lesson3_exe_1.test_uniq_chars('')
		self.assertTrue(result)
  		
	def test_test_uniq_chars_no_repeat(self):
		result=lesson3_exe_1.test_uniq_chars('bar')
		self.assertTrue(result)
  		
	def test_test_uniq_chars_repeat(self):
		result=lesson3_exe_1.test_uniq_chars('foo')
		self.assertFalse(result)
