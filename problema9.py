#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

af=bf=cf=0

Found=False
for a in range(3,1000):
	for b in range(1,a):
		if ((a*a)+(b*b))==pow(1000-a-b,2):
			af=a
			bf=b
			cf=1000-a-b
			Found=True
			break
	if (Found):
		break
		
print "Triplet found: (" + str(af) +","+str(bf)+","+str(cf)+")"
		
print "Product:" + str(af*bf*cf)
			
			
				