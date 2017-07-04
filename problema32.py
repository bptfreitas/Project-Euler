#!/usr/bin/python


#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


import itertools


digits = [1,2,3,4,5,6,7,8,9]

permuts = itertools.permutations(digits)

divs = [(x,y) for x,y in itertools.permutations(range(len(digits)),2) if x+1<y and x > 0]

for d in divs: 

	print d

	dmult1 = digits[0:d[0]]
	dmult2 = digits[d[0]:d[1]]
	dmul = digits[d[1]:len(digits)]

	mult1 = sum([ p*q for p,q in zip(reversed(dmult1),[ pow(10,i) for i in range(len(dmult1))])])
	mult2 = sum([ p*q for p,q in zip(reversed(dmult2),[ pow(10,i) for i in range(len(dmult2))])])
	mul = sum([ p*q for p,q in zip(reversed(dmul),[ pow(10,i) for i in range(len(dmul))])])

	print mult1 , "*", mult2, "=", mul	


pannums = []	
for pm in permuts:

	#print "----", pm

	for d in divs:

		dmult1 =pm[0:d[0]]
		dmult2 = pm[d[0]:d[1]]
		dmul = pm[d[1]:len(digits)]

		if len(dmul)>=len(dmult1) and len(dmul)>=len(dmult2):
			mult1 = sum([ p*q for p,q in zip(reversed(dmult1),[ pow(10,i) for i in range(len(dmult1))])])
			mult2 = sum([ p*q for p,q in zip(reversed(dmult2),[ pow(10,i) for i in range(len(dmult2))])])
			mul = sum([ p*q for p,q in zip(reversed(dmul),[ pow(10,i) for i in range(len(dmul))])])

			#print mult1 , "*", mult2, "=", mul

			if mult1*mult2 == mul and mul not in pannums:
				print "Pandigital number found: ", mult1 , "*", mult2, "=", mul
				pannums.append(mul)

		#print mult1 , "*", mult2, "=", mul

print pannums
print sum(pannums)
