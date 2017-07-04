#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#Find the largest palindrome made from the product of two 3-digit numbers.

a=999
b=999

def is_pal(a,b):
	s_num=str(a*b)
	
	siz=len(s_num)
	
	left=s_num[0:(siz/2)]
	if (siz%2==0):		
		right=s_num[-1:(-siz/2)-1:-1]
	else:	
		right=s_num[-1:(-siz/2):-1]

	print s_num +": size "+ str(siz) +", left " + left +", right " + right

	if (left==right):
		print "Found:" + str(s_num) + "=" + str(a) + "*" + str(b)
		return True
	else:
		return False


pals=list()
while (a>499):
	if (is_pal(a,b)==True):	
		pals.append(a*b)
		print pals		

	b-=1
	if (b==99):
		a,b=a-1,999

print "Complete list:"
for i in sorted(pals):
	print i
	
