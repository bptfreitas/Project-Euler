#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the first term in the Fibonacci sequence to contain 1000 digits?

pen = [1]
ult = [1]

termo = 2

while True:
	carry=0
	for d in range(len(ult)):
		soma = pen[d] + ult[d] + carry
		
		pen[d]=ult[d]

		ult[d]=soma%10

		if (soma>=10):
			carry = soma/10
		else:
			carry = 0

	termo+=1	
	
	if (carry > 0):
		ult.append(carry)
		pen.append(0)

	#for d in ult[::-1]:
	#	print d,

	if len(ult)>=1000:
		break

print "Primeiro termo de soma dos digitos de fib com 1000 digitos:" + str(termo)
	
