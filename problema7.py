#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import euler

#2 is the only even number, so we start at 3
pos=10000
num=3

print str(pos+1) + "th prime is:" 
while (pos>0):
	if (euler.is_prime(num)):
		pos-=1	
	num+=2

print str(num-2)

	