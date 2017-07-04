

def fact(num):
	return num*fact(num-1) if num>1 else 1

class FactNum
	def get_factors(num, remove_num =True, debug = False):
		limit=num/2

		if (debug):
			print "Calculating factors of:" + str(num)

		primes=get_primes2(limit,debug)

		n=num
		factors={}
		for div in primes:
			first=True
			
			while (n%div==0):
				n/=div
				if (first==True):
					factors[div]=1
					first=False
				else:			
					factors[div]+=1

		if factors == {} :
			factors={num:1}	

		if remove_num and num in factors.keys():
			#print "\tRemoving" +  str(num) + "from factor list"
			del factors[num]
		
		if (debug):
			print "Factors of " + str(num) +":"
			print factors

		return factors

	def __init__(self,Number):
		

#tests if a number is prime
def is_prime(num, debug=False):	
	if (num%2==0):
		return False
	for div in range(3,num/2,2):
		if (num%div==0):
			return False
	return True	

#returns all primes between a lower bound and an upper bound 
def get_primes(bound,debug=False):
	pos_prime_facs=range(3,bound+1,2)

	primes=[2]
	for n in pos_prime_facs:
		if (is_prime(n)):
			primes.append(n)

	if (debug):
		print "Primes between "+str(1)+" and "+str(bound)+":"
		print primes

	return primes

#returns all primes using the sieve of erasthotenes
def get_primes2(bound,debug=False):
	nspam=[j for j in range(2,bound+1)]

	if (debug):
		print nspam
		print len(nspam)

	i=j=0	
	while i<len(nspam):

		while (i <len(nspam)) and nspam[i]==0:
			i+=1

		if i<len(nspam):

			if (debug):
				print "prime:" + str(nspam[i])	
			
			num=nspam[i]		
			for j in range(i+num,len(nspam),num):
				nspam[j]=0

			i+=1

	if (debug):
		print nspam

	return [ n for n in nspam if n!=0 ] 
				

#factorizes a number
#returns a dictionary whose keys are the bases, for which are associated powers


#returns the divisors of a number
def get_divisors(num,proper=True,debug=False):
	facs=get_factors(num)

	exp_facs=[]
	for k in facs.keys():
		for i in range(facs[k]):
			exp_facs.append(k)

	if (debug):
		print "Expanded Factors:"
		print exp_facs

	divs=[1]

	for f in exp_facs:
		tmp_divs=list(divs)
		for d in tmp_divs:
			if f*d not in tmp_divs:
				divs.append(f*d)
				if (debug):
					print "New divisors list"
					print divs

	if (proper):
		divs.remove(num)

	return sorted(divs)



	
