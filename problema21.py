#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

import euler

def d(n):
	return sum(euler.get_divisors(n))


print euler.get_divisors(284)

print sum(euler.get_divisors(284))

limit=10000

perc=5
step=perc*limit/100
cp=0

a=1

amics=[]

print "Starting..."

for a in range(1,limit+1):
	
	b=d(a)
	if a==d(b) and a!=b:
		print "Pair:" + str(a) + " and " + str(b)
		if (a not in amics):
			amics.append(a)
		if (b not in amics):
			amics.append(b)
		

print "Sum of amicables:"
print sum(amics)
		

