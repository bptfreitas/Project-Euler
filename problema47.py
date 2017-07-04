#!/usr/bin/python

#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 * 7
#15 = 3 * 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2 * 7 * 23
#645 = 3 * 5 * 43
#646 = 2 * 17 * 19.

#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import euler

from math import sqrt
from math import floor
from euler import get_primes2
from euler import ceil
from euler import log
from euler import prod
from itertools import combinations
from itertools import product

# lets fucking think for a second ... quais sao as combinacoes de restos possiveis?
# 0 1 2 3 - multiplo de 4 2


def problema47_v1(n):
	count = 0
	numbers = []
	while True:
		factors = euler.get_factors(n)

		if len(factors.keys())==4:
			#print factors.keys()
			count+=1
			numbers.append(n)
		else:
			count=0
			del numbers[:]

		if count==4:
			print numbers
			break
		else:
			n+=1


def problema47_v2(limit,num_factors):
		max_potency = int(floor(log(limit)/log(2)))
		print "max_potency:", max_potency

		Primes = [p for p in get_primes2(int(pow(2,max_potency))) if p < sqrt(limit) ]

		max_potencies = { p: int(floor(log(limit)/log(p))) for p in Primes } 

		#print max_potencies

		#print "Primes:", Primes

		#all_potencies = [ pot for pot in product([ p for p in range(1,max_potency+1) ],repeat=num_factors) ]

		#print [ p for p in all_potencies ]
		
		all_numbers = []
		passes = 0
		for factors in combinations(Primes,num_factors):						
			if prod(factors)<limit:
				passes+=1
				for potencies in product( *[ range(1,max_potencies[f]+1) for f in factors] ):
					#print "\t", potencies
					number = prod([ pow(b,p) for (b,p) in zip(factors,potencies) ])
					if number<limit:
						#print number
						all_numbers.append(number)
			if passes%1000==0:
				passes = 0
				print "Update: number list has ", len(all_numbers), "candidates"

		sorted_numbers = sorted(all_numbers)

		print "Ended candidates generation. Starting sequential search ..."

		for ini in range(0,len(sorted_numbers)-num_factors):
			sequence = []
			sequence.append(sorted_numbers[ini])
			for seq in range(ini-1):
				if sorted_numbers[ini+seq]+1==sorted_numbers[ini+seq+1]:
					sequence.append(sorted_numbers[ini+seq+1])
				else:
					break
			if len(sequence)==num_factors:
				print sequence
				break
			else:
				del sequence[:]

def problema47_v3(limit,seq_len):
	nspam=[j for j in range(2,limit+1)]

	#print nspam

	i=j=0
	found = False
	while i<len(nspam):

		while (i <len(nspam)) and nspam[i]<0:
			if abs(nspam[i])==seq_len:
				#print "->", i
				sequence = []
				for seq in range(i-seq_len+1,i+1):
					#print seq, 
					if abs(nspam[seq])==seq_len:
						sequence.append(seq+2)
					else:
						break
				if len(sequence)==seq_len:
					print sequence
					found = True
				#else:
					#print 
			if found:
				break
			else:
				i+=1

		if found: 
			break

		if i<len(nspam):
			num=nspam[i]
			for j in range(i+num,len(nspam),num):
				if nspam[j]>0:
					nspam[j]=-1
				else:
					nspam[j]-=1

			i+=1

	#print nspam

													
problema47_v3(1000000,4)

if False:
	primes = get_primes2(50)
	max_potencies = { p: int(floor(log(50)/log(p))) for p in primes if p<50 }
	print max_potencies 

	for factors in combinations(primes,2):
		for potencies in product( *[ range(1,max_potencies[f]+1) for f in factors] ):
			#print [ range(1,max_potencies[f]+1) for f in factors ]
			print factors, "\n\t", potencies


