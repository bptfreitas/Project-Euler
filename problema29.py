#!/usr/bin/python
#Euler published the remarkable quadratic formula:


import math
import euler
import itertools

vec = range(2,101)

nums = []

for pair in itertools.product(vec,vec):
	base = pair[0]
	exp = pair[1]

	print base, "^", exp

	num=euler.get_factors(base,False)

	#print num

	for x in num.keys():
		num[x]=num[x]*exp

	print num

	nums.append(num)

prod = itertools.product(nums,nums)

uniq_nums = []
for p in prod:
	#print p[0].keys() , "/",p[1].keys()
	if p[0].keys() == p[1].keys():
		igual = True
		for k in p[0].keys():
			if p[0][k]!=p[1][k]:
				igual = False
				break
		if igual==True and p[0] not in uniq_nums:
			#print "igual:" , p[0]
			uniq_nums.append(p[0])

for n in nums:
	if n not in uniq_nums:
		uniq_nums.append(n)

print len(uniq_nums)
	

