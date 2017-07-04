#!/usr/bin/python

#In England the currency is made up of pound,  and pence, p, and there are eight coins in general circulation:

#   1p, 2p, 5p, 10p, 20p, 50p, (100p) and (200p).

#It is possible to make 2 in the following way:

#    1x + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

#How many different ways can 2 be made using any number of coins?

import itertools

def iterar2(value,weights,qtd=[],kini=0,i=''):

	if len(qtd) == 0:
		qtd = [0 for x in range(len(weights))]
		qtd[0]=1

	#string = str(i) + "Pesos:" + str(qtd)

	soma = sum([p*q for p,q in zip(qtd, weights)])

	if soma > value:
		return 0
	elif soma == value:
		return 1
	else:
		s = 0

		qtd_tmp=list(qtd)
		qtd_tmp[kini]-=1
				
		for k in range(kini,len(weights)):
			novo_qtd =list(qtd)
			novo_qtd[k]+=1
			#print novo_qtd
		
			s += iterar(value,weights,novo_qtd,k,i+'--')
								
		#print i, "Current sum:", 

		return s

def iterar(value,weights,qtd=[],kini=0,i=''):

	if len(qtd) == 0:
		qtd = [0 for x in range(len(weights))]

	string = str(i) + "Pesos:" + str(qtd)

	soma = sum([p*q for p,q in zip(qtd, weights)])

	if soma > value:
		return 0
	elif soma == value:
		return 1
	else:
		s = 0
				
		for k in range(kini,len(weights)):
			novo_qtd =list(qtd)
			novo_qtd[k]+=1
			#print novo_qtd
		
			s += iterar(value,weights,novo_qtd,k,i+'--')
								
		#print i, "Current sum:", 

		return s


weights = [200,100,50,20,10,5,2,1]

print iterar(200,weights)

