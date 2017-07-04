#!/usr/bin/python


#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17

#Find the sum of all 0 to 9 pandigital numbers with this property.

import euler

from math import sqrt
from euler import is_prime
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations

divs = [2,3,5,7,11,13,17]
soma=0
#for p in [(1,4,0,6,3,5,7,2,8,9)]:
for p in permutations(range(10)):
	count=0
	for s in range(7):
		test = sum([ d*pot for d,pot in zip([p[s+1],p[s+2],p[s+3]],reversed([pow(10,i) for i in range(3)]) )])		
		if test%divs[s]==0:
			count+=1
		else:
			break

	if count==7:
		number = sum([ d*pot for d,pot in zip(p,reversed([pow(10,i) for i in range(len(p))]) ) ])
		print "Found: ", number
		soma+=number
		
print "Sum is:", soma
			
