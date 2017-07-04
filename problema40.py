#!/usr/bin/python

#Take the number 192 and multiply it by each of 1, 2, and 3:

#    192 x 1 = 192
#    192 x 2 = 384
#    192 x 3 = 576

#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

from euler import get_primes2
#from euler import fat
from math import log
from math import ceil
from math import floor
from itertools import permutations
from itertools import combinations

num = 1

positions = [ pow(10,i) for i in range(7) ]

#positions = [3, 7, 10, 20]

print positions

constant = ''
constant_len = 0
index = 0
prod=1
digits = []
while index<len(positions):
	#constant+=str(num)
	constant_len+=len(str(num))

	if constant_len >= positions[index]:
		digit = str(num)[len(str(num))-(constant_len-positions[index])-1]
		digits.append(digit)
		prod*=int(digit)
		index+=1

	num+=1

print constant
print digits
print prod
