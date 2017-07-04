#!/usr/bin/python 

from math import floor,sqrt

from itertools import combinations,permutations

RANGE=10

def divisors(n):
	return [1,n]

solutions=[]

for D in range(1,RANGE+1):
	for y in xrange(1,1000):
		divs = divisors(D*y*y)
		for d in xrange(len(divs)-1):
			xminus1=divs[d];
			xplus1=divs[d+1];

			if xminus1+2==xplus1 and xplus1==D*y*y:
				x
	
	
	


		



	


