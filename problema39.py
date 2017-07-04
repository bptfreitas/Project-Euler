#!/usr/bin/python

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p <= 1000, is the number of solutions maximised?



import euler

from math import sqrt
from euler import is_prime
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations

def gen_squares(limiti,limits=0):
	n=limiti
	if limits==0:
		limits=limiti
	
	while n<limits:
		n+=1
		if n>=limiti:
			yield n*n
		
max_count = 0
for p in range(1,1000):
	#print "Testing p=",p , "..."
	count = 0
	for a in range(1,p+1):		
		for b in range(a+1,p/2):
			c = sqrt(pow(a,2)+pow(b,2))
			#print "a=",a, "/b=", b, "/c=", c
			if a+b+c == p :
				#print a, "+", b, "+", c , " = ", p
				count +=1

	if count>max_count:
		max_count = count
		print "New maximum found: ", count, " for p=", p
			
			

