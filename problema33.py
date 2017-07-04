#!/usr/bin/python


#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import itertools
import euler
from euler import MDC

def reduzir(num,den,wrong_num,wrong_den):

	mdc = MDC(num,den)
	wrong_mdc = MDC(wrong_num,wrong_den)

	if (num//mdc == wrong_num//wrong_mdc) and (den//mdc == wrong_den//wrong_mdc):
		print num,"/",den," -> ",num//mdc, "/", den//mdc

digits = range(10)

for num,den in [(x,y) for x,y in itertools.product(range(10,100),repeat=2) ]:
	un = num%10
	dn = den%10

	if num<den and not (un%10==0 or dn%10==0):

		if (num//10==den%10):
			reduzir(num,den,num%10,den//10)
		
		if (num%10==den//10):
			reduzir(num,den,num//10,den%10)

		if (num//10==den//10):
			reduzir(num,den,num%10,den%10)

		if (num%10==den%10):
			reduzir(num,den,num//10,den//10)

						
