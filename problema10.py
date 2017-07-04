#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import time
import pickle

debug=False
limit=2000000
#limit=11200

#first prime numbers 
prime_list=[2,3,5,7,11]

#files for statistics
prime_file=open('primes.txt','w')

for p in prime_list:
	prime_file.write(str(p)+'\n')

bench_file=open('bench.txt','w')


#searches only odd numbers for primes - even ones are obviously not
progress=0
start_time = time.time()
for num in range(13,limit+1,2):

	last=0
	is_prime=True

	#converts the number to string and computes the sum of all it's digits
	num_str=str(num)

	s0_sum=sum(int(d) for d in num_str[0:len(num_str):2])
	s1_sum=sum(int(d) for d in num_str[1:len(num_str):2])

	if debug:
		print "----Testing: " + str(num)
		print "s0 digits sum:" + str(s0_sum)
		print "s1 digits sum:" + str(s1_sum)

	#if a number ends in 5, the sum of its digits is divisible by 3, or their difference is not divisible by 11, then the number is not a prime
	if (num_str[len(num_str)-1]!='5') and ((s0_sum+s1_sum)%3!=0) and (((s0_sum-s1_sum)%11!=0)):

		# it's a possibly prime, so computes the list of primes lower that half's the number value
		lower_primes=[]
		for prime in prime_list:			
			if prime<=num/2:
				lower_primes.append(prime)
			else:
				break
	
		#if one of the primes computed above divides the number, then it is not a prime
		for div in lower_primes:			
			if (num%div==0):				
				is_prime=False
				last=num
				break

		#if a number is a prime, adds to the list of primes			
		if (is_prime):			
			if debug:
				print "New prime: " + str(num)
			prime_list.append(num)
			prime_file.write(str(num)+'\n')

		if debug:			
			print "lower factors:"
			print lower_primes
			print "primes:"
			print prime_list
	else:
		if debug:
			print "Last digit:" + num_str[len(num_str)-1] 

	progress+=1
	if progress%10000==0:
		end_time = time.time()

		print str(progress)

		bench_file.write(str(progress)+'\t'+str(end_time-start_time)+'\n')
		bench_file.close()

		prime_file.close()
				
		prime_file=open('primes.txt','a')
		bench_file=open('bench.txt','a')

		start_time= time.time()
		
print "Sum:" + str(sum(prime for prime in prime_list))
	
