#!/usr/bin/python

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


import argparse
import sys

from euler import get_primes2,binary_search,fact

from itertools import izip,combinations,product

from bisect import insort_left,insort

from math import log


def find_prime_pair_sets_v3(prime_limit,set_length):
	
	Primes = get_primes2(prime_limit)
			
	# filtering primes that can be composed by other 2 primes

	prime_pairs = {}
	prime_seeds = []
	
	for p in Primes:
		for index in xrange(1,len(str(p))):
			p1 = str(p)[0:index]
			p2 = str(p)[index:len(str(p))]
						
			#print p2+p1, " ", p1, " ", p2
			if binary_search(int(p1),Primes) and binary_search(int(p2),Primes):
			
				if len(str(int(p1+p2)))==len(str(p)) and len(str(int(p2+p1)))==len(str(p)) and binary_search(int(p2+p1),Primes):
					key1 = int(p1+p2)
					value1 = (int(p1),int(p2))
					
					if key1 not in prime_pairs.keys():
						prime_pairs[key1]=[ value1 ]
					elif value1 not in prime_pairs[key1]:
						prime_pairs[key1].append( value1 )											
				
					key2 = int(p2+p1)
					value2 = (int(p2),int(p1))
											
					if key2 not in prime_pairs.keys():					
						prime_pairs[key2]=[ value2 ]
					elif value2 not in prime_pairs[key2]:				
						prime_pairs[key2].append( value2 )
	
	if False:
		for key in sorted(prime_pairs.keys()):												
			print key,": ", prime_pairs[key]
		
	# put all primes pairs that generate primes on only 1 list
	prime_seeds = []
	all_prime_pairs = []
	for pairs in prime_pairs.itervalues():
		for (p1,p2) in pairs:
			if int(str(p1)+str(p2))<prime_limit and p1<p2:
				insort(all_prime_pairs,(p1,p2))
	
	if False:
		print all_prime_pairs	

	# put all primes that can be generated on a single list
	if False:
		all_primes = [  ]
		for a,b in all_prime_pairs:
			if a not in all_primes:
				insort(all_primes,a)
			if b not in all_primes:
				insort(all_primes,b)

	index = 0
	lowest_sum = sys.maxint

	while index<len(all_prime_pairs):

		prime=all_prime_pairs[index][0]

		test_vector = [ (a,b) for (a,b) in all_prime_pairs if a==prime ]

		#print test_vector

		for comb in combinations(test_vector,set_length-1):

			primes = [ b for (a,b) in comb ]

			#print primes

			found = True
			for comb2 in combinations(primes,2):
				if not binary_search(comb2,all_prime_pairs):
					found=False
					break
									
			if found:
				primes.insert(0,prime)
				soma = sum(primes)
				if soma<lowest_sum:
					print "\tNew minimum found:", soma, " for ", primes
					lowest_sum=soma
				
		index+=len(test_vector)
	
		
		
		
		
		
		


def find_prime_pair_sets_v2(prime_limit,set_length):
	
	Primes = get_primes2(prime_limit)
	
	# filtering primes that can be composed by other 2 primes
	
	#print Primes
	
	prime_pairs = []
	prime_seeds = []	
	
	for p in Primes:
		for index in xrange(1,len(str(p))):
			p1 = str(p)[0:index]
			p2 = str(p)[index:len(str(p))]
			
			#print p2+p1, " ", p1, " ", p2
			
			if binary_search(int(p2+p1),Primes) and binary_search(int(p1),Primes) and binary_search(int(p2),Primes):
				if not binary_search(int(p1),prime_seeds):
					insort_left(prime_seeds,int(p1))
					
				if not binary_search(int(p2),prime_seeds):
					insort_left(prime_seeds,int(p2))
					
				if not binary_search(p,prime_pairs):
					insort_left(prime_pairs,int(p))
					
				if not binary_search(int(p2+p1),prime_pairs):
					insort_left(prime_pairs,int(p2+p1))					
				
						
	#print prime_pairs
	
	lowest_sum = sys.maxint
	for set in combinations(prime_seeds,set_length):
		#print set
		stop = False
		for (p1,p2) in combinations(set,2):
			#print p1,",",p2
			prime1 = str(p1)+str(p2)
			prime2 = str(p2)+str(p1)
			#print prime1,",",prime2
								
			if not binary_search(int(prime1),prime_pairs) or not binary_search(int(prime2),prime_pairs):
				stop=True
				break
		if stop:
			continue
			
		print set
		
		Sum = sum(set)
		
		if Sum<lowest_sum:
			lowest_sum = Sum
			print "New lowest: ", lowest_sum
			
		
		
	


def find_prime_pair_sets_v1(prime_limit,set_length):
	
	Primes = get_primes2(prime_limit)
	
	Primes = [ p for p in Primes if p!=2 and p!=5 ]	
	
	hard_limit = log(Primes[len(Primes)-1])

	lowest_sum = sum( [ Primes[i] for i in xrange(len(Primes)-1,len(Primes)-5,-1) ] )
	
	for prime_set in combinations(Primes,set_length):
					
		get_lowest_sum = True
	
		#print [ p for p in prime_set ]
			
		for (p1,p2) in combinations(prime_set,2):
			perm1 = int(str(p1)+str(p2))
			perm2 = int(str(p2)+str(p1))
			
			if log(perm1)>hard_limit or log(perm2)>hard_limit:
				get_lowest_sum = False
				break
								
			if not binary_search(perm1,Primes) or not binary_search(perm2,Primes):
				get_lowest_sum = False
				break
			
		if get_lowest_sum:
			Sum = sum([ p for p in prime_set])
			if Sum < lowest_sum:
				lowest_sum = Sum
				print "Lowest sum is: ", Sum, " for prime set: ", [ p for p in prime_set]
			
			
			
Description = "Finds the lowest sum for a set of 'SET_LEN' primes for which any two primes concatenate to produce another prime"
parser = argparse.ArgumentParser(description=Description)
parser.add_argument('--setlen',nargs='?',type=int)
parser.add_argument('--limit',nargs='?',type=int)

args = parser.parse_args()

try:
	setlen = int(args.setlen)
	limit = int(args.limit)
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	
	find_prime_pair_sets_v3(limit,setlen)
		
		

