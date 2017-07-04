#!/usr/bin/python

#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

import argparse
import sys

from euler import is_palindrome
from Number import Number
from Number import testNumber
from math import log,floor


from itertools import izip,combinations,product

def get_max_digital_sum(maxbase,maxexp):
	max_digit_sum = 1
	for (b,e) in product(range(1,maxbase),repeat=2):
	
		#print "(", b, ",", e , ")"
		r = long(b**e)
			
		digit_sum = sum([ int(d) for d in str(r) ])
		
		if digit_sum>max_digit_sum:
			max_digit_sum = digit_sum
			print "Maximum digit sum is (", b, ",", e, ") : ", digit_sum			


tests = testNumber()

parser = argparse.ArgumentParser(description='finds the prime ratio along  the diagonals of a square spiral')
parser.add_argument('--maxbase',nargs='?',type=int)
parser.add_argument('--maxexp',nargs='?',type=int)

args = parser.parse_args()

try:
	base = int(args.maxbase)
	exp = int(args.maxexp)
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	

	get_max_digital_sum(base,exp)



