#!/usr/bin/python
# encoding: latin1

#The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

import argparse

from math import floor,ceil,sqrt,log				
from itertools import takewhile,imap,count,izip
from euler import binary_search

def calc_perms(seed,cubes,digits=[]):
	if digits==[]:
		digits = [ digit for digit in str(seed) ]

		all_perms = calc_perms('',cubes,digits)
		return all_perms
	elif len(digits)>1:
		perms = []
		for i in range(len(digits)):
			digit = digits[i]
			updated_digits=list(digits)
			del updated_digits[i]
			perms = perms + calc_perms(seed+digit,cubes,updated_digits)

		return perms
	else:
		perm = seed+digits[0]
		if len(perm)==len(seed) and binary_search(int(perm),cubes):
			return [perm]
		else:
			return []		

def count_digits(number):
	counter = {} 
	for d in set(str(number)):
		counter[d]=sum([ 1 for x in str(number) if x==d ])
	return counter

parser = argparse.ArgumentParser(description='finds the cube with exactly "perm" permutations cubes as well')
parser.add_argument('--climit',nargs='?',type=int,default=1000)
parser.add_argument('--maxperms',nargs='?',type=int,default=2)

args = parser.parse_args()

try:
	limit = int(args.climit)
	maxperms = int(args.maxperms)
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	
	cubes = [ i**3 for i in range(1,limit+1) ]

	cubes_digits = { c : count_digits(c) for c in cubes }	

	while len(cubes)>0:
		cube = cubes[0]
		a = cubes_digits[cube]
		a_values = [ v for v in a.values() ]
		a_items	 = [ v for v in a.iteritems() ]

		perms = []		
		for i in xrange(1,len(cubes)):
			b=cubes_digits[cubes[i]]			
			b_values = [ v for v in b.values() ]
			b_items	 = [ v for v in b.iteritems() ]

			if sum(a_values) == sum(b_values) and len(a_items)==len(b_items):
				is_perm = True
				for (x,y) in izip(a_items,b_items):
					if x!=y:
						is_perm=False
						break
				 
				if is_perm:
					perms.append(cubes[i])
			elif sum(a_values)>sum(b_values):
				break

		if len(perms)==maxperms:
			print "Found: ", cube, perms
			break
		else:
			del cubes[0]
			for p in perms:
				del cubes[cubes.index(p)]
