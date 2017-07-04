#!/usr/bin/python

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

import euler

from math import sqrt
from euler import is_prime
from euler import is_pandigital
from euler import is_permutation
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations

# how to make it quicker: eliminate unecessary r2 tests
def problema49(num_of_digits):
	primes = get_primes2(pow(10,num_of_digits))

	primes_to_test = [ p for p in primes if p>pow(10,num_of_digits-1) ]

	for p1 in range(len(primes_to_test)-2):
		prime1 = primes_to_test[p1]
		for p2 in range(p1+1,len(primes_to_test)-1):
			prime2 = primes_to_test[p2]
			r1 = r1 = prime2-prime1 			
			for p3 in range(p2+1,len(primes_to_test)):			
				prime3 = primes_to_test[p3]
								
				r2 = prime3-prime2

				if (r1 == r2):
					if is_permutation(prime1,prime2) and is_permutation(prime2,prime3):
						print "(", prime1, ") + " , r1 , " = (" , prime2 , ") + " , r2 , " = (" , prime3, ")"
						print str(prime1)+str(prime2)+str(prime3)
				elif r2>r1:
					break


#print is_permutation(1451,1541)
problema49(4)


