#!/usr/bin/python

#There are exactly ten ways of selecting three from five, 12345:

#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

#In combinatorics, we use the notation, 5C3 = 10.

#In general,

#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

#How many, not necessarily distinct, values of  nCr, for 1 n  100, are greater than one-million?


import euler

from math import sqrt
from euler import binary_search
from euler import is_prime
from euler import is_permutation
from euler import gen_pandigitals
from euler import get_primes2
from euler import fact
from itertools import permutations
from itertools import combinations

	

def problema53(lines):

	pascal = [ [ 0 for x in range(lines) ] for y in range(lines) ]
		
	for n in xrange(0,lines):
		pascal[n][0]=1
		for r in xrange(1,n+1):
			pascal[n][r]=pascal[n-1][r-1]+pascal[n-1][r]		

	print pascal[23][10]

	counter = 0
	for x in xrange(lines):
		for y in xrange(lines):
			if pascal[x][y]>1000000:
				counter+=1	

	print counter
								
problema53(101)
