#!/usr/bin/python

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?


# inicio eh igual a 1
num = [1]

for i in range(1000):
	carry = 0
	for d in range(len(num)):
		digit = num[d]
		mul2 = digit * 2 + carry

		num[d]=mul2%10

		if (mul2>=10):
			carry = mul2/10
		else:
			carry = 0
	
	if (carry > 0):
		num.append(carry)

	#print num

print "Soma dos digitos do numero 2^1000:" + str(sum(num))
