#!/usr/bin/python
#Euler published the remarkable quadratic formula:


import math
import euler
import itertools

def matrix(n):
	if n == 0:
		mat = [ [ 1 for x in range(1)] for y in range(1) ]
		return mat
	else:
		matant = matrix(n-1)
		mat = [ [0 for x in range(2*n+1)] for y in range(2*n+1) ]

		for x in range(1,len(mat)-1):
			for y in range(1,len(mat)-1):
				mat[x][y]=matant[x-1][y-1]

		dim = 2*n+1

		init = mat[1][dim-2]

		for x in range(1,dim):
			init+=1
			mat[x][dim-1]=init

		for y in range(dim-2,0,-1):
			init+=1
			mat[dim-1][y]=init

		for x in range(dim-1,0,-1):
			init+=1
			mat[x][0]=init

		for y in range(dim):
			init+=1
			mat[0][y]=init
			

		return mat

M = matrix(500)

#for x in range(len(M)):
#	for y in range(len(M[x])):
#		print str(M[x][y]), "\t",
#	print "\n"

soma = 0

for x in range(len(M)):
	for y in range(len(M[x])):
		if x == y or len(M)-x-1 == y :
			soma += M[x][y]

print soma

