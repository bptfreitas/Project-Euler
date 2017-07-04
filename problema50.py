#!/usr/bin/python

#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13

#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import euler

from math import sqrt
from euler import is_prime
from euler import is_pandigital
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations


def problema50_v1(limit):
	Primes = euler.get_primes2(limit)

	max_chain_length = 0
	max_chain_prime = 0

	for prime in Primes:
		#print prime
		primes_to_test = [ x for x in Primes if x < prime ]

		ini = i = test = 0 	
		primes_list = []
		#print primes_to_test
		while ini < len(primes_to_test) -1 and (primes_to_test[ini]+primes_to_test[ini+1])<prime:
			test+=primes_to_test[i]
			primes_list.append(primes_to_test[i])
			#print primes_list
			if test > prime:
				ini+=1
				i=ini
				test = 0
				del primes_list[:]
			elif test == prime:
				#print "Prime ", prime, " is composed by the sum: ", primes_list
				chain_length = len(primes_list)
				if chain_length>max_chain_length:
					max_chain_length = chain_length
					max_chain_prime = prime
			else:
				i+=1

	print "Maximum chain found was: "
	print "\tPrime:\t", max_chain_prime
	print "\tLength:\t", max_chain_length


def problema50_v2(limit):
	primes = euler.get_primes2(limit)

	max_sum_len = 0
	max_prime = 0
	for pi in range(len(primes)):
		i = pi
		sum_primes = 0
		while sum_primes < limit and i<len(primes):
			sum_primes+=primes[i]
			i+=1
				
			if sum_primes in primes:
				sum_len=i-pi+1
				if sum_len>max_sum_len:
					max_sum_len=sum_len
					max_prime = sum_primes
					print "Max prime sum update: ", max_prime, " with length ", max_sum_len


problema50_v2(1000000)

