#!/usr/bin/python

#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

import math
import euler
import itertools
import sys
import argparse

from euler import get_primes2
from euler import binary_search
from euler import is_prime

def problema58_v2(ratio,limit):

	rate = 2
	number = 1
	total_primes = 0
	total_numbers = 1

	best_ratio = 1.0

	while number<limit:
		number+=rate
		total_numbers += 1
		
		if is_prime(number):
			total_primes+=1

		if (total_numbers-1)%4==0:
			ratio_now = float(total_primes)/float(total_numbers)
			
			if ratio_now<best_ratio:
				best_ratio = ratio_now		
				
			if (ratio_now<ratio):			
				break
				
			rate+=2			

	
	print "Rate: " + str(rate)
	print "Best ratio: " + str(best_ratio)
	print "Dimension is: ", rate+1


def matrix(percentage,n=0,matant=[],total_primes=0):
	if n == 0:
		mat = [ [ 1 for x in range(1)] for y in range(1) ]
		matrix(percentage,1,mat,0)
	else:
		mat = [ [0 for x in range(2*n+1)] for y in range(2*n+1) ]

		for x in range(1,len(mat)-1):
			for y in range(1,len(mat)-1):
				mat[x][y]=matant[x-1][y-1]

		dim = 2*n+1

		init = matant[len(matant)-1][len(matant)-1]

		for x in xrange(dim-1,0,-1):			
			mat[x][dim-1]=init
			init+=1

		for y in xrange(dim-1,0,-1):			
			mat[0][y]=init
			init+=1

		for x in xrange(0,dim-1):			
			mat[x][0]=init
			init+=1

		for y in xrange(dim):	
			mat[dim-1][y]=init
			init+=1

		numbers=4*n + 1
		primes =0
		Primes = get_primes2(dim*dim)

		for comb in itertools.product([0,len(mat)-1],repeat=2):
			p1 = comb[0]
			p2 = comb[1]			
			if mat[p1][p2] in Primes:				
				primes+=1
				#print mat[p1][p2]

		calc = float(primes+total_primes)/numbers
		#print dim, "=", calc

		if calc<percentage:
			print "Side is:" , (dim+1)
		else:
			matrix(percentage,n+1,mat,total_primes+primes)


parser = argparse.ArgumentParser(description='finds the prime ratio along  the diagonals of a square spiral')
parser.add_argument('--ratio',nargs='?',type=float)
parser.add_argument('--limit',nargs='?',type=int)

args = parser.parse_args()

try:
	ratio = float(args.ratio)
	limit = int(args.limit)
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	
	problema58_v2(ratio,limit)

