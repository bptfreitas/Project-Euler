#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

#What is the total of all the name scores in the file?

import string

f=open("names22.txt","r")

nlist=[]
for line in f:
	nlist.append(line)

names=[]
for n in nlist:
	names=names+n.split(',')

tmp=[]
while (len(names)>0):
	tmp.append(names.pop().strip('\"').upper())

names=sorted(tmp)
print names

letters=string.uppercase
value={}
for i in range(len(letters)):
	 value[letters[i]]=i+1

soma=0
position=1
for name in names:
	soma_nome=0
	for letter in name:
		soma_nome+=value[letter]

	soma+=soma_nome*position
	position+=1

print str(soma)





	
