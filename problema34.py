#!/usr/bin/python

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.


from euler import fact
from itertools import permutations
from itertools import combinations_with_replacement

fats={}
for i in range(0,10):
	print i
	fats[i]=fact(i)

num_digits=1
num = 9
num_f9 = fats[9]
while num<num_f9:
	num=10*num+9
	num_f9+=fats[9]
	num_digits+=1

print "maximum number of digits is: " + str(num_digits)

s = 0
nums = []
#num_digits=2
limite = pow(10,num_digits+1)

soma_numeros = 0
for i in range(1,limite):
	#print i
	#perm = combinations_with_replacement(fats,i)

	num = i
	num_f = 0 

	while num!=0:
		digit = num%10
		num_f += fats[digit]
		num//=10

	if num_f == i:
		print "Adicionei : " + str(i)
		nums.append(i)

print sum(nums)
