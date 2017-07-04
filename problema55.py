#!/usr/bin/python

from euler import is_palindrome

def problema55(limit=10000):

	total = 0
	
	for n in xrange(limit):
		counter = 0
		print n
		is_Lychrel = False
		while True:
			n = n + sum([ int(d)*pow(10,e) for (d,e) in zip([di for di in str(n) ] ,range(len(str(n)))) ]) 

			if is_palindrome(n):	
				is_Lychrel = False
				break
			else:
				counter+=1
				if counter == 50:
					is_Lychrel = True
					break
		
		if is_Lychrel:
			total+=1
			
	return total

for test in [ 121, 47, 444 ]:
	print test, ": ", is_palindrome(test)

print problema55()
