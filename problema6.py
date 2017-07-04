#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import euler

sum_of_sq=0
sq_of_sum=0

for num in range(1,101):
	sum_of_sq+=(num*num)
	sq_of_sum+=num
	
sq_of_sum*=sq_of_sum

print "Sum of the squares: " + str(sum_of_sq)
print "Square of the sum: " + str(sq_of_sum)
print "Difference: " + str(sq_of_sum-sum_of_sq)

