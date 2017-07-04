#!/usr/bin/python

#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13

#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import euler

from math import sqrt
from euler import binary_search
from euler import is_prime
from euler import is_permutation
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations
from itertools import combinations


def problema52(limit):
		
	for n in xrange(1,limit):
		if is_permutation(n,2*n) and is_permutation(n,3*n) and is_permutation(n,4*n) and is_permutation(n,5*n) and is_permutation(n,6*n):
			print n
			break
			
		


		
problema52(1000000)
