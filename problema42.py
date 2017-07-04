#!/usr/bin/python

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?


import euler
import string

from euler import is_pandigital
from euler import get_primes2
from math import sqrt

num = 1

#The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

# if it is a triangle number, then the 2nd degree equation has solutions
def is_triangle_number(number):
	i=0
	soma = 0
	while i<= number:
		soma += i
		i+=1
		yield soma

for test in [123,233.4,55,10]:
	print test, " = ", is_triangle_number(test)

letter2pos = {}

letters = string.uppercase
	
for i in range(len(letters)):
	letter2pos[letters[i]]=i+1

count_twords = 0
for line in open('words.txt','r'):
	for l in line.rsplit(','):
		word = l.rstrip("\"").strip("\"")
		sum_letters = sum([ letter2pos[letter] for letter in word])
		for t in is_triangle_number(sum_letters):
			if t==sum_letters:
				count_twords+=1
				
print count_twords

