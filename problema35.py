#!/usr/bin/python

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?


from euler import get_primes2
from itertools import permutations
from itertools import combinations

primes = get_primes2(1000000)

#print primes

# MAGIC! Eliminates all primes with even digits!
primes = [ x for x in primes if sum([ int(i) for i in str(x) if int(i)%2==0 ])==0 ]

#print primes

all_ciclic_primes = []

for max_digits in range(1,7):

	primes_in_range = [ x for x in primes if x>=pow(10,max_digits-1) and x < pow(10,max_digits) ]

	print "Max digits for primes: ", max_digits

	print "Bound is : [", pow(10,max_digits-1) , "," , pow(10,max_digits) , ")"

	#print primes_in_range

	#MAGIC! All digit rotations in 1 line!
	all_digit_rotations = [ range(i,max_digits)+range(0,i) for i in range(0,max_digits) ]

	print all_digit_rotations

	for prime in primes_in_range:

		p = str(prime)

		#print "Number is: ", p

		is_ciclic = True
		ciclic_primes = []
		for digit_perm in all_digit_rotations:

			num = sum([ int(p[digit_perm[i]])*pow(10,len(digit_perm)-i-1) for i in range(len(digit_perm)) ])

			if num in primes:
				#print "\tDigit permutation ", digit_perm, " is prime: ", num
				ciclic_primes.append(num)
			else:
				#print "\tDigit permutation ", digit_perm, " is NOT prime: ", num, " - Aborting "
				is_ciclic=False
				break

		if is_ciclic:
			for ciclic in ciclic_primes:
				if ciclic not in all_ciclic_primes:
					all_ciclic_primes.append(ciclic)

all_ciclic_primes.sort()
print all_ciclic_primes
print len(all_ciclic_primes)
