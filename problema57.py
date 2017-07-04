#!/usr/bin/python

from euler import is_palindrome
from euler import Number
from math import log,floor
from itertools import izip

def problema57(limit):
	num = 1
	den = 2
	counter = 0
	for exp in xrange(limit):
		aux = num
		num = den
		den = 2*den+aux

		nump = num + den
		denp = den

		if len(str(nump))>len(str(denp)):
			counter+=1

		#print nump, "/", denp

	return counter
					
print Number('aas')
