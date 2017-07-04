#!/usr/bin/python

#Take the number 192 and multiply it by each of 1, 2, and 3:

#    192 x 1 = 192
#    192 x 2 = 384
#    192 x 3 = 576

#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

from euler import get_primes2
from euler import is_pandigital
from math import log
from math import ceil
from math import floor
from itertools import permutations
from itertools import combinations

for test in [192384576,293845761,993845761,1192384576,92384576]:
	print test, ": ", is_pandigital(test)

integer = 1

while integer < 1000000000:
	n = 1
	prod_concat = ''
	while True:
		prod = integer*n
		prod_concat += str(prod)
		n+=1

		if len(prod_concat)>=9:
			break

	if len(prod_concat)==9 and is_pandigital(int(prod_concat)):
		print integer, "*", n, " = ", prod_concat

	integer+=1
	
	


