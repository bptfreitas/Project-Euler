#!/usr/bin/python


#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#    1634 = 14 + 64 + 34 + 44
#    8208 = 84 + 24 + 04 + 84
#    9474 = 94 + 44 + 74 + 44

#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math
import euler
import itertools

from itertools import product

pot5={}
len_pot5={}
for i in range(0,10):
	print i
	pot5[i]=pow(i,5)
	len_pot5[i]=len(str(pot5[i]))

print pot5
	

#searches the maximum number possible using the rules
num_digits=1
num = 9
num_pot5 = pot5[9]
while num<num_pot5:
	num=10*num+9
	num_pot5+=pot5[9]
	num_digits+=1

print "Maximum digit fifth power length: ",num_digits

print len_pot5

sum_pot5 = 0
for number_length in range(2,num_digits+1):
	max_len = 1
	while max_len<=9:
		if len_pot5[max_len] > number_length:
			break
		else:
			max_len+=1

	# creates the vector of possible digits to use and then all its possible combinations
	digits_to_use = [ x for x in range(max_len) ]

	print "Maximum length of number is", number_length, " - digits to use: ", digits_to_use

	numbers = product(digits_to_use,repeat=number_length)

	for number in numbers:		
		if number[0]!=0:
			#print number
			num = sum([ number[i]*pow(10,len(number)-i-1) for i in range(len(number)) ])
			num_pot5 = sum([ pot5[i] for i in number ])

			if num == num_pot5:
				print "Adding: ", num
				sum_pot5+=num		
		

print "Sum is:", sum_pot5




