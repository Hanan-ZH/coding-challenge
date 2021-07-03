"""
This module is to test the impelemtation of fold function: fold(function, sequence, initalvalue(optional))

Tests are for: subtraction function: sensitive to list order and variables order inside function
			  when initial value is None & list is empty
			  
"""
import unittest
import fold

class TestFold(unittest.TestCase):

	# test for left fold for a subtraction function with initial value:
	def test_foldl_initvalue(self):
		result = fold.fold(lambda x,y: x - y , [1, 2, 3], 0 )
		self.assertEqual(result, -6 )

	# test for left fold for a subtraction function without initial value:
	def test_foldl_no_initvalue(self):
		result = fold.fold(lambda x,y: x - y , [1, 2, 3] )
		self.assertEqual(result, -4 )


	# test for right fold for a subtraction function with initial value:
	def test_foldr_initvalue(self):
		result = fold.fold(lambda x,y: y - x , [1, 2, 3][::-1], 0 )
		self.assertEqual(result, 2 )

	# test for right fold for a subtraction function without initial value:
	def test_foldr_no_initvalue(self):
		result = fold.fold(lambda x,y: y - x , [1, 2, 3][::-1] )
		self.assertEqual(result, 2 )


	# test for left fold for a subtraction function without initial value and empty list
	def test_foldl_no_initvalue_empty_sequence(self):
		with self.assertRaises(TypeError):
		     fold.fold(lambda x,y: x - y , [] )
			 

if __name__ == "__main__":
	unittest.main()

