#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#Resposta: 4179871
import euler

def get_abundants(limit):
	abund=[12]
	nums=[]
	for n in range(13,limit+1):
		divs=euler.get_divisors(n)
		if sum(divs)>n:
			abund.append(n)

	return abund

LIMIT=28123

abunds=get_abundants(LIMIT)
nums_as_sums_of_abund=[]

#print abunds

for i in range(len(abunds)):
	for j in range(len(abunds)-i):
		num=abunds[i]+abunds[i+j]
		if num<=LIMIT: 
			if num not in nums_as_sums_of_abund:
				#print str(num)
				nums_as_sums_of_abund.append(num) 

#print str(nums_as_sums_of_abund)
nums=range(1,LIMIT+1)

nums_not_sums_of_abund=[n for n in nums if n not in nums_as_sums_of_abund]
#print str(nums_not_sums_of_abund)

print "Sum of not abundants:" + str(sum(nums_not_sums_of_abund))

