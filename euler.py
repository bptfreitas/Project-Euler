
import string
import operator

from math import log
from math import ceil
from math import floor
from math import sqrt

from itertools import permutations
from itertools import combinations
from bisect import bisect_left


# productory function
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

# simple binary search algorithm for lists, returns true if item x exists on ordered list a
def binary_search(x,a):
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return True
	else:
		return False

# calculates the factorial of 'num'
def fact(num):
	return num*fact(num-1) if num>1 else 1

#tests if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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


#returns all primes using the sieve of erasthotenes - using a generator
def generate_primes(bound,start=3,debug=False):
	nspam=[j for j in range(3,bound+1,2)]

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
				

#factorizes a number
#returns a dictionary whose keys are the bases, for which are associated powers
def get_factors(num, remove_num = False, remove_one = False, debug = False):
	limit=num

	if (debug):
		print "Calculating factors of:" + str(num)

	primes=get_primes2(limit,debug)

	n=num
	factors={}
	factors[1]=1

	if num in primes:
		factors[num]=1
	else:
		for div in primes:
			first=True
			
			while (n%div==0):
				n/=div
				if (first==True):
					factors[div]=1
					first=False
				else:			
					factors[div]+=1

	if remove_num:
		#print "\tRemoving" +  str(num) + "from factor list"
		del factors[num]

	if remove_one:
		del factors[1]
		
	if (debug):
		print "Factors of " + str(num) +":"
		print factors

	return factors

# calculates how many divisors a number has
def get_total_divisors(num,proper=True):
	facs=get_factors(num)

	facs.pop(1)

	d=1

	for p in facs.keys():
		d*=(facs[p]+1)

	return d


# simplify a division
def simplify_div(num,den):
	for f in facts_num.keys():
		if f in facts_den.keys():
			d = facts_num[f] if facts_num[f]<= facts_den[f] else facts_den[f]
			facts_num[f]-= d
			facts_den[f]-= d


# returns the MMC of 
def MMC(vecNum):
	MMC = 1
	divisor = 2
	while True:
		dividiu = False
		for i in range(len(vecNum)):
			if vecNum[i]%divisor==0:
				vecNum[i]=vecNum[i]/divisor
				dividiu=True

		if dividiu:
			MMC=MMC*divisor
		else:
			divisor=divisor+1
				
	return MMC

def MDC(n1,n2):
	num1 = n1
	num2 = n2

	if n1 == 0  or n2 == 0:
		return 1

	MDC = 1
	divisor = 2
	while num1>1 or num2>1:
		if num1%divisor == 0 and num2%divisor == 0:
			MDC*=divisor
			num1//=divisor
			num2//=divisor
		elif num1%divisor == 0:
			num1//=divisor
		elif num2%divisor == 0:
			num2//=divisor
		else:
			divisor+=1

	return MDC

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

	exp_facs.remove(1)
	divs=[1]

	for f in exp_facs:
		tmp_divs=list(divs)
		for d in tmp_divs:
			if f*d not in tmp_divs:
				divs.append(f*d)
				if (debug):
					print "New divisors list"
					print divs

	return sorted(divs)

# returns if a number is pandigital
def is_pandigital(number,vector=[]):

	if len(vector) == 0:
		vector=[ x for x in range(1,len(str(number))+1) ]

	#print vector
	if len(str(number))>9 or len(str(number))!=len(vector):
		return False
	elif len(str(number))==1:
		return number in vector
	else:
		digit=int(str(number)[0])
		if digit in vector:
			return is_pandigital(int(str(number)[1:]),vector= [ x for x in vector if x!=digit ])
		else:
			return False

def gen_pandigitals(num,digits=[],numbers=[]):
	# doesnt work
	if num>9:
		return []

	print digits

	if digits == []:	
		digits = range(1,num+1)
		numbers = range(1,num+1)
		
		for d in digits:
			numbers.extend(gen_pandigitals(num,[ i for i in digits if d!= i],numbers))
		return numbers
	else:
		new_numbers = []
		for i in digits:
			for n in numbers:
				new_numbers.append(int(str(n)+str(i)))

			if len(digits)>1:
				new_numbers.extend(gen_pandigitals(num,[ d for d in digits if d!= i],new_numbers))

		return new_numbers

def is_triangular(number):
	root = sqrt(8*number+1)
	if round(root)==root:
		return True
	else:
		return False

def pentagonal(n):
	return n*(3*n-1)/2

def is_pentagonal(number):
	n = (sqrt(24*number+1)+1)/6
	if round(n)==n:
		return True
	else:
		return False

def gen_pentagonals(limit,limit_max=0):
	n = 0 if limit_max == 0 else limit
	maximum = limit if limit_max==0 else limit_max
	while n< maximum:
		yield n*(3*n-1)/2
		n+=1

def hexagonal(n):
	return n*(2*n-1)

def is_hexagonal(number):
	n = (sqrt(8*number+1)+1)/4
	if round(n)==n:
		return True
	else:
		return False	

# return True if "one" is a permutation of "another"
def is_permutation(one,another):
	if len(str(one))!=len(str(another)):
		return False
	if len(str(another))==1 and len(str(another))==1:
		return True	if one == another else False
	else:
		digit = str(one)[0]
		#print digit, " from ", int(str(one)) , " in " , int(str(another)) , "?"
		if digit not in str(another):
			return False
		else:
			#print int(string.join(str(another).split(digit,1),''))
			return is_permutation(int(str(one)[1:]),int(int(string.join(str(another).split(digit,1),''))))

def is_palindrome(num):
	number = str(num)
	for x in xrange(len(str(num))):
		if number[x]!=number[len(number)-1-x]: 
			return False
	return True

def get_rotations(length):
	return [ range(i,length)+range(0,i) for i in range(0,length) ]	
		


		




