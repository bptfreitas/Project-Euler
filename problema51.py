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
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations
from itertools import combinations


def problema51():
	Primes = get_primes2(1000000)
		
	max_chain = 0

	for prime in Primes:
		#print "Prime: ", prime
		
		total_len = len(str(prime))
				
		for comb_len in xrange(1,total_len):

			for comb in combinations(range(total_len),comb_len):
				strnum = [ x for x in str(prime) ]
				#print "before: ", strnum
				#print "combination: ", comb
				chain = 0
				numbers = []

				digits = range(10)

				for d in digits:
					#print "\tdigit: ", d
					for c in comb:
						strnum[c]=str(d)

					#print strnum

					number = sum([ int(d)*pow(10,p) for (d,p) in zip(strnum,[ p for p in range(total_len-1,-1,-1) ])])

					#print "\tafter: ", number

					if strnum[0]!='0' and binary_search(number,Primes):
						#print "\tFound: ", number, " for combination ", comb
						numbers.append(number)
				
				if len(numbers)>max_chain:
					print "Total chain length: ", chain, " for prime", prime
					print "\tCombination: ", comb 
					print "\t", numbers
					max_chain = len(numbers)
					if max_chain == 8:
						break

			if max_chain == 8:
				break					

		if max_chain == 8:
			break					
		
problema51()
