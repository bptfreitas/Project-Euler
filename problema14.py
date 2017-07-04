

lens=[[0,0]]
for sn in range(1000000):
	if not sn%10000:
		print sn
	
	n=sn
	cl=1
	
	while (n>1):
		if not n%2:
			n/=2		
		else:
			n=3*n+1
		
		cl+=1
	
	if cl>(lens[0][1]):
		print str(cl) + " > " + str(lens[0][1])
		lens.pop()
		lens.append([sn,cl])
		
		
print "Cadeia mais longa: " + str(lens[0][0])