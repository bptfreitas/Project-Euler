#!/usr/bin/python

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?


import euler

from euler import is_prime
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations

num = 1

for test in [123,124,2143,12345,12344]:
	print test, ': ' , is_pandigital(test)

def problem41():
	primes_to_test = []
	
	for i in range(9,1,-1):
		all_numbers = [ p for p in permutations(range(1,i+1)) ]
		print "Testing " + str(i) + "-digit pandigital primes ..."
		#primes_to_test = [ x for x in primes if len(str(x))==i ]

		found = False
		for tu in reversed(sorted(all_numbers)):
			n = sum([d*p for d,p in zip(tu,reversed([ pow(10,i) for i in range(len(tu)) ])  )])
			#print n

			found = False
			if is_prime( n ):
				print n			
				break 

		if found:
			break

print [ p for p in permutations(range(1,4)) ]
problem41()
