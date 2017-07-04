#!/usr/bin/python

#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2*12
#15 = 7 + 2*22
#21 = 3 + 2*32
#25 = 7 + 2*32
#27 = 19 + 2*22
#33 = 31 + 2*12

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


import euler

from math import sqrt
from euler import is_prime
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations

order = 100
primes = get_primes2(order)

n = 9
while True:
	if n>order:
		order*=10
		primes = get_primes2(order)

	found = False
	if n not in primes:
		primes_to_test = [ p for p in primes if p<n]
	
		for p in primes_to_test:
			n_minus_p = n - p
			if n_minus_p%2==0:
				square = n_minus_p/2
				if sqrt(square)==round(sqrt(square)):
					found=True	
					break
		if not found:
			print "smallest composite is:", n
			break
		else:	
			print n , "=", n_minus_p , "+ 2*" , square
			n+=2
	else:
		n+=2

			
