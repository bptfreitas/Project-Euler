#!/usr/bin/python 

from math import floor,sqrt

from itertools import combinations,permutations

listn=[]

GONLEN=5

numbers = range(1,2*GONLEN+1)

somas = [ (x+GONLEN,x,x+1)  for x in range(GONLEN-1) ]
somas.extend( [ (2*GONLEN-1,GONLEN-1,0) ] )

print somas

max_string='0'
all_nums = []

for perm in permutations(numbers):
	#print perm
	todas_parciais = []
	todas_somas = []
	for serie in somas:
		soma= sum( [ perm[i] for i in serie ] )
		todas_somas.append( soma )
		todas_parciais.append( int( ''.join([ str(perm[i]) for i in serie ]) )  )
		
		if soma == todas_somas[0]:
			continue
		else:
			break

	if len(todas_somas)<GONLEN or (todas_somas[GONLEN-1]!=todas_somas[GONLEN-2]) :
		continue

	#print todas_parciais

	div=todas_parciais.index(min(todas_parciais))
	todas_parciais_ord = todas_parciais[div:]
	todas_parciais_ord.extend( todas_parciais[:div] )

	#print todas_parciais
	string=''.join( str(p) for p in todas_parciais_ord )

	if len(string)==16 and string not in all_nums:
		all_nums.append(string)

for n in all_nums:
	print n
		



	


