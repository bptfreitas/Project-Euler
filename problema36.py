#!/usr/bin/python

#The decimal number, 585 = 1001001001 2 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

from euler import get_primes2
from math import log
from math import ceil
from math import floor
from itertools import permutations
from itertools import combinations

limit = 1000000
max_binary_digits = int(ceil(log(limit)/log(2))/2)
max_binary_digits = 4

all_double_palin = [1]
for number in range(pow(2,max_binary_digits)):
	binary = bin(number)[2:]
	print binary

	for middle in ['','0','1']:

		palin_binary = binary + middle + binary[::-1]

		print "\t middle(" + middle + "):" + palin_binary

		decimal = str(sum( int(palin_binary[i])*pow(2,len(palin_binary)-i-1) for i in range(len(palin_binary)) ))

		print "\t" + decimal

		is_double_palin = True
		for i in range(len(decimal)):
			if decimal[i]!=decimal[len(decimal)-i-1]:
				is_double_palin = False
				break

		print "\t", is_double_palin
		if is_double_palin and palin_binary[0]!='0' and int(decimal)<=limit and (int(decimal) not in all_double_palin):
			all_double_palin.append(int(decimal))


print sum(all_double_palin)
