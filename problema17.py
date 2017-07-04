#!/usr/bin/python

unidades=dezenas={}

unidades[0]=''
unidades[1]='one'
unidades[2]='two'
unidades[3]='three'
unidades[4]='four'
unidades[5]='five'
unidades[6]='six'
unidades[7]='seven'
unidades[8]='eight'
unidades[9]='nine'
dezenas[10]='ten'
dezenas[11]='eleven'
dezenas[12]='twelve'
dezenas[13]='thirteen'
dezenas[14]='fourteen'
dezenas[15]='fifteen'
dezenas[16]='sixteen'
dezenas[17]='seventeen'
dezenas[18]='eighteen'
dezenas[19]='nineteen'
dezenas[20]='twenty'
dezenas[30]='thirty'
dezenas[40]='forty'
dezenas[50]='fifty'
dezenas[60]='sixty'
dezenas[70]='seventy'
dezenas[80]='eighty'
dezenas[90]='ninety'

soma=0
snuml=0
for num in range(1,1001):	

	cent=num/100
	deze=((num/10)%10)*10
	unid=num%10

	nome=''

	if cent>0:
		if (cent<=9):
			nome+=unidades[cent]+'hundred'		
		else:
			nome+='onethousand'			

		if deze>0 or unid>0:
			nome+='and'

	if deze>=20:
		nome+=dezenas[deze]+unidades[unid]
	elif deze>=10:
		nome+=dezenas[deze+unid]
	else:
		nome+=unidades[unid]

	print str(num)+": "+str(cent)+"/"+str(deze)+"/"+str(unid) + "=" +nome + " ("+str(len(nome))+")"

	soma+=len(nome)

print soma

