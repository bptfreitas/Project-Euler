

limit=4000000
sum=num=0

ant=num=1

while (num<limit):
	num, ant = ant+num,num
	print str(num) + " " + str(ant) 
	if (num%2==0):
		sum+=num
	
print sum