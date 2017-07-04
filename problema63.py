#!/usr/bin/python

#The 5-digit number, 16807=75, is also a fifth power. 

#Similarly, the 9-digit number, 134217728=89, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?



import argparse
import sys

from euler import get_primes2,binary_search,fact

from itertools import izip,combinations,product

from bisect import insort_left,insort

from math import log,ceil
			
Description = "Finds the lowest sum for a set of 'SET_LEN' primes for which any two primes concatenate to produce another prime"
parser = argparse.ArgumentParser(description=Description)
#parser.add_argument('--setlen',nargs='?',type=int)
parser.add_argument('--limit',nargs='?',type=int)

args = parser.parse_args()

try:
	#start = int(args.start)
	limit = int(args.limit)
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	
	pot = 1
	c = 0 

	total = 1 # computing 1^1
	
	while c<limit:
		#print "*** computing potency ", pot, " ***"
		n = 1
		entered = False
		while ceil(pot*log(n)/log(10))<=pot:			
			if ceil(pot*log(n)/log(10))==pot and n%10!=0:
				print "\t", n,"^",pot, "=", n**pot, "(", len(str(n**pot)), ")"
				total+=1
			n+=1

		pot+=1
		c+=1

	print total
