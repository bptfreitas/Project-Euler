#!/usr/bin/python

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


from euler import get_primes2
from math import log
from math import ceil
from math import floor
from itertools import permutations
from itertools import combinations


def is_left_truncable(number,primes_list):
	#print number
	if len(str(number))==1:
		return number in primes_list
	else:
		return False if number not in primes_list else is_left_truncable(int(str(number)[1:]),primes)

def is_right_truncable(number,primes_list):
	#print number
	if len(str(number))==1:
		return number in primes_list
	else:
		max_left = len(str(number))-1
		return False if number not in primes_list else is_right_truncable(int(str(number)[0:max_left]),primes)

def search_truncable_primes(primes,vector=[2,3,5,7],depth=''):
	#print depth, vector
	truncable_primes = []
	for number in vector:
		for digit in [1,2,3,5,7,9]:
			# creates new number and test if is truncable on both directions
			left_num = int(str(digit) + str(number))
			#print depth, left_num
			if left_num in primes:
				#print depth+'\t', left_num
				left_chains = search_truncable_primes(primes,vector=[left_num],depth=depth+'\t')
				left_chains.append(left_num)
				for chain in left_chains:
					if is_right_truncable(chain,primes):
						truncable_primes.append(chain)

	return truncable_primes if len(truncable_primes)>0 else vector

		
primes = get_primes2(1000000)

# MAGIC! Eliminates all primes with even digits!
#primes = [ x for x in primes if sum([ int(i) for i in str(x) if int(i)%2==0 ])==0 ]

print is_left_truncable(3797,primes)
print is_right_truncable(3797,primes)

print sum(set(search_truncable_primes(primes)))
			


