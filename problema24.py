#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically #or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#Resposta: 2783915460
import euler

digits=[]
for d in range(10):
	digits.append(str(d))
print digits


i=0
s=0
limit=1000000
perm=9
numero=''
p=euler.fact(perm)
while len(digits)>0:
	print "Digito " +str(digits[i])+"..."
	
	if s+p>=limit:
		numero+=str(digits[i])
		digits.remove(digits[i])
		print "Numero: " + numero

		perm=len(digits)-1
		p=euler.fact(perm)
		print "Nova permutacao : " + str(perm) +"/"+str(p)

		print "Posicao:" + str(s)
		i=0
	else:
		s+=p
		i+=1		
		
		


	

