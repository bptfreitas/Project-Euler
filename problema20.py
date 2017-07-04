#!/usr/bin/python

#n! 

#For example, 10! = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

import euler


def d(n):
	return sum(euler.get_divisors(n))

limit=100

fact_factors={}

print "Starting..."

for n in range(1,limit+1):

	n_factors=euler.get_factors(n)
	
	for base in n_factors.keys():
		if base in fact_factors.keys():
			fact_factors[base]+=n_factors[base]
		else:
			fact_factors[base]=n_factors[base]

# remove powers of 10 from the number 
fact_factors[2]-=fact_factors[5]
fact_factors[5]=0

# get the number without powers of 10
N=1

for b in fact_factors.keys():
	N*=b**fact_factors[b]
	print b**fact_factors[b]

print 'Factorial:'+str(N)

# sum it up
fact_sum=0
while (N>0):
	fact_sum+=N%10
	N/=10

print 'Sum of digits:' + str(fact_sum)
