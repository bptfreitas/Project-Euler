#!/usr/bin/python
#Euler published the remarkable quadratic formula:

#n**2 + n + 41

#It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

#Using computers, the incredible formula  n**2+ 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

#Considering quadratics of the form:

#n**2 + an + b, where |a|  1000 and |b|  1000

#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import math
import euler
import itertools

from euler import binary_search

def formulae(a,b,n):
	return (pn-p0-pow(n,2))/(n)

#vec = [range(-999,-1,2),2,range(3,999,2)]
#vec = [ 1, 41, -79, 1601]

def problema27():
	vecA = [x for x in range(-999,1000)]

	Np = 1000000
	Primes=euler.get_primes2(Np)
	max_chain_length=0
	max_prime_A = 0
	max_prime_B = 0

	#print Primes

	vecB = [ x for x in Primes if x<=1000 ]
	vecB.extend([-x for x in vecB])

	#print vecB

	counter = 0
	for comb in itertools.product(vecA,vecA):
		a = comb[0]
		b = comb[1]	

		#if counter%1000==0:
		#	print "Testing (", a, ",", b, ") ..."

		counter+=1
	
		n = 0
		last_prime = -1	
		chain_length = 0

		while True:
			fx = abs(n*n+a*n+b)
			
			if binary_search(fx,Primes):
				chain_length+=1
				n+=1
			else:
				if fx>Primes[len(Primes)-1]:
					print "Prime list updated:\n\tOld length = " , len(Primes)
					Primes=euler.get_primes2(fx+1)
					print "\tOld length = " , len(Primes)
				else:
					break
	
		if max_chain_length<=chain_length:
			max_chain_length=chain_length
			max_prime_A = a
			max_prime_B = b
		
			print "Maximum chain is with A=", a," and B=",b,"(",max_chain_length,"). a*b=", a*b


problema27()

#vecA = [x for x in range(-10,11)]

#for x in itertools.product(vecA,vecA):
#	print x
