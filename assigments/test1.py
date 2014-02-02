from src import string_op
import unittest


class Test(unittest.TestCase):
	def test_one_word(self):
		result = string_op('Today')
		assert result == 'Today'
		assert isinstance(result, str)
		print '1st test case for one word  is passed'

	def test_many_word(self):
		result = string_op('Today is my birthday')
		assert result == 'birthday my is Today'
		assert isinstance(result, str)
		print '2nd test case for many is passed'

	
	def test_more_space(self):
		result = string_op('Today is   my birthday')
		assert result == 'birthday my   is Today'
		assert isinstance(result, str)
		print '3th test case for more space is passed'
	
	def test_spacial_with_char(self):
		result = string_op('@Today@ @is@ @my@ @birthday@')
		assert result == '@birthday@ @my@ @is@ @Today@'
		assert isinstance(result, str)
		print '4th test case for spacial char is passed'
	
	def test_math_string(self):
		result = string_op('1 2 3 4 5')
		assert result == '5 4 3 2 1'
		assert isinstance(result, str)
		print '5th test case for math string is passed'




if __name__ == '__main__':
	unittest.main()
