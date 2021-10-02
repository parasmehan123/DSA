	# CSE 101 - IP HW2
	# K-Map Minimization test cases
	# Name: HIMANSHU GARG
	# Roll Number: 2018337
	# Section: B
	# Group: 2
	# Date: 16th October 2018

"""
this python file is used to test different cases and to find out whether 'minFunc' is correctly coded or not...
"""

import unittest
from HW2_2018337 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		'''to test "minFunc" function'''
		self.assertEqual(minFunc(4, "(4,8,10,11,12,15)d(9,14)"),"wx'+wy+xy'z'")
		self.assertEqual(minFunc(2, "(0,1,2,3)d-"),"1")
		self.assertEqual(minFunc(4, "(6,8,9,10,11,12,13,14)d-"),"wx'+wy'+xyz'")
		self.assertEqual(minFunc(3, "(0,1,2)d-"),"w'x'+w'y'")
		self.assertEqual(minFunc(2, "(0,1)d(2)"),"w'")
		self.assertEqual(minFunc(4, "(0,1,10,12,14)d(5,7)"),"w'x'y'+wxz'+wyz'")
		self.assertEqual(minFunc(3, "(2,3,5,6,7)d(0,1,4)"),"1")
		self.assertEqual(minFunc(3, "(0,1,3)d(2)"),"w'")
		self.assertEqual(minFunc(2, "()d(2,3)"),"0")
		self.assertEqual(minFunc(4, "(4,6)d(0,1,3,7,8,10,13,14)"),"w'xz'")



if __name__=='__main__':
	unittest.main()
