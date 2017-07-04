#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num=float(600851475143)
limit=num/2
div=2

def is_prime(num):
	i=3
	while (i<num/2):
		if (num%i==0):
			return False
		i+=2
	return True

largest=0
i=float(3)
while (i<limit):
	if (num%i==0):
		if (is_prime(i)):
			largest=i
			print largest
	i+=2

print largest
	


	
	
