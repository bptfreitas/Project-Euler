
import string
import operator

from math import log
from math import log10
from math import ceil
from math import floor
from math import sqrt

from itertools import permutations
from itertools import combinations
from bisect import bisect_left

import sys
import types

class Number:
	digits = []

	iterator = 0
	

	def __init__(self,number = None,digit_count=-1):	
		self.digits = []
		
		if number != None:
			try:
				int(number)
			except Exception:
				error_msg = "parameter 'number' must be an integer"
				raise ValueError(error_msg)
			else:		
				while number>0:
					self.digits.append(number%10)
					number//=10

	def __len__(self):		
		return len(self.digits)
		
	def __iter__(self):
		self.iterator = len(self.digits)-1
		return self

	def next(self):
		if self.iterator<0:      
			raise StopIteration
		else:
			self.iterator-=1
			return self.digits[self.iterator+1]
		
	def __str__(self):
		return ''.join(reversed([ str(x) for x in self.digits ]))

	def __getitem__(self,key):
		if type(key) is not types.IntType:
			raise TypeError("Invalid type")
				
		if key<0 or key>=len(self.digits):
			raise IndexError("Invalid index")
			
		return self.digits[len(self)-1-key]

	def __setitem__(self,key,value):		
		if type(key) is not types.IntType:
			msg = "Invalid type for 'index': got " + str(type(key)) 
			raise TypeError(msg)
			
		if type(value) is not types.IntType:
			msg = "Invalid type for 'value': got " + str(type(value)) 
			raise TypeError(msg)
	
		if value<0 or value>9:
			raise ValueError("Invalid 'value': must be between 0 and 9")							

		index=len(self.digits)-1-key
		
		if index>=len(self.digits) or index<0:
			msg = "'index' must be between 0 and " + str(len(self.digits)-1)
			raise IndexError(msg)

		self.digits[index]=int(value)
		
	def append(self,value):
		if type(value) is not types.IntType:
			msg = "Invalid type for 'value': got " + str(type(value)) 
			raise TypeError(msg)
		if value<0 or value>9:
			raise ValueError("Invalid 'value': must be between 0 and 9")		
			
		self.digits.append(value)
		
	def getNumber(self):
		
		return sum( [ self.digits[i]*pow(10,i) for i in xrange(len(self.digits)) ])
						
	def __add__(self,number):	
		if type(number) is not type(self):
			raise TypeError("Invalid type for sum")
	
		carry = 0
		result = Number()
		
		for i in xrange(len(self) if len(self)<len(number) else len(number) ):
			s = number[i]+self[i] + carry
			carry = s//10
			s = s%10
			
			result.append(s)

		if len(self)<len(number):			
			for i in xrange(len(number) - len(self)):			
				result.append(len(self)+1)
			
		if carry>0:
			result.append(carry)
			
			
		return result
		

class testNumber:
	test_vector = []	
	
	def __init(self,fileout):
		self.file = sys.stdout 
	
	def _print(self,num2test):
		n = Number(num2test)
		print n	
		
		del n
		
	def _len(self,num2test):
		n = Number(num2test)
		print "n:", n
		print "len: ", len(n)
		
		del n

	def _iterators(self,num2test):
		for x in Number(num2test):
			print x,

	def _get(self,num2test ) :
	
				
		msg = "*** Testing __get__  method *** \n"
		
		test = Number(num2test)

		for index in xrange(len(test)):
			msg+= str(index)+': ' + str(test[index]) + '\n'
							
		msg+='\n'
		try:
			x = test[-1]
		except IndexError:
			msg+= "PASS: invalid index exception at index "  + str(-1) + "\n"
		else:
			msg+= "FAIL: invalid index exception - got " +str(x) +"at index "  + str(-1) + "\n"
			
		try:
			x = test[len(test)]
		except IndexError:
			msg+= "PASS: invalid index exception at index " + str(len(test)) + "\n"
		else:
			msg+= "FAIL: invalid index exception - got " + str(x) + " at index " + str(len(test))
			
		for l in test:
			msg+= str(l)
			
		print msg	

		del test
			
	def _set(self,num2test):
		test_set = Number(num2test)
		
		print "*** Testing __set__  method ***"
		
		print test_set
		
		try:			
			test_set[0]=10
		except ValueError:
			print "PASS: caught a number greater than 9 assignment"
		else:
			print "FAIL: didn't get number greater than 9 assignment"

		try:
			test_set[0]=-1
		except ValueError:
			print "PASS: negative number assignment"
		else:
			print "FAIL: negative number assignment"

		try:
			test_set[0]="1.2"
		except TypeError:
			print "PASS: invalid type for 'value' assignment"			
		else:
			print "FAIL: invalid type for 'value' assignment"
			
		try: 
			test_set[-1]=2
		except IndexError:
			print "PASS: negative key assignment"			
		else:
			print "FAIL: negative key assignment"
			
		try: 
			test_set[len(test_set)]=2
		except IndexError:
			print "PASS: greater than maximum index assignment"			
		else:
			print "FAIL: greater than maximum index assignment"					
	
		for x in xrange(len(test_set)):
			print test_set[x], 
			test_set[x]=9-test_set[x]	

		print 

		for x in xrange(len(test_set)):
			print test_set[x],
			
		del test_set
	
	def _add(self,num1,num2):
	
		test_add1 = Number(num1)
		test_add2 = Number(num2)
		
		r = test_add1 + test_add2
		
		print r
		
