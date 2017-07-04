#!/usr/bin/python


import euler

from math import sqrt
from euler import is_pentagonal
from euler import hexagonal
from itertools import permutations
	
# starts testing all hexagonals starting from H143

n = 144

while True:
	number = hexagonal(n)
	if is_pentagonal(number):
		print number
		break
	else:
		n+=1			
