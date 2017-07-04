#!/usr/bin/python 

from math import floor,sqrt,log

def PeriodicSquareRoot(x,verbose=False):
	r=sqrt(x)
	a0=a=int(floor(r))

	if verbose:
		print x, " = ", a, " ", 

	n=0
	while True:	
		
		r=1/(r-a)
		a=int(floor(r))
		n+=1

		if verbose:
			print a, " ", 

		if a==2*a0:
			break

	if verbose:
		print 

	return n

MAX=10000
if True:
	count=0
	numbers = range(2,MAX+1)
	n=2
	while n*n<=MAX+1:
		numbers.remove(n*n)
		n+=1

	#print numbers

	for N in numbers:
		#print "N:", N
		n=PeriodicSquareRoot(N,False)
		if n%2==1:
			count+=1 

	print "count: ", count
else:
	print PeriodicSquareRoot2(sqrt(13))
			

		

	

