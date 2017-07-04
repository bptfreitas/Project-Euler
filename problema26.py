#!/usr/bin/python
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def divide(num,div,debug=False):
	n=num	
	q=0
	
	while n>=div:
		n-=div
		q+=1

	#print str(n) + " " + str(q)

	dizima=[]
	divs=[]
	diz = []

	qtd = 0
	while True:
		n*=10
		r=0
		while n>=div:
			n-=div
			r+=1

		#divs.append(n)
		dizima.append(r)

		#print "Hello"

		#print divs
		#print dizima

		isDizima = False

		if n == 0:
			break 

		for i in range(len(divs)/2):
			#divs_ini = divs[len(divs)-1-2*i-1:len(divs)-1-i]
			#divs_end = divs[len(divs)-1-i:len(divs)]

			diz_ini = dizima[len(dizima)-1-2*i-1:len(dizima)-1-i]
			diz_end = dizima[len(dizima)-1-i:len(dizima)]

			if diz_ini == diz_end:
				isDizima=True
				diz = diz_end
				break

		if isDizima:
			break

	return q, r, diz

longest = []
for d in range(1,1000):
	q,r,diz = divide(1,d)

	if len(diz)>len(longest):
		longest = diz
		print "UPDATE: d = " , d, "len(longest) = ", len(longest)

		
