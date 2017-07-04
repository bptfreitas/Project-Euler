#!/usr/bin/python

import FactNum

################################
# Testing iterators
################################

n1 = FactNum.DigitNum(123)

if n1[0] != 3 or n1[1] != 2 or n1[2] != 1:
	raise ValueError("Expected: 123, got:",n1[0],n1[1],n1[2])

n2 = FactNum.DigitNum(122)

################################
# Testing equal operator (__eq__)
################################

testVec = [ [122,122], [122,123], [222,122]]
resVec = [ True, False, False ]

print "-- Testing equal operator:"
for i in range(len(testVec)):

	n1 = FactNum.DigitNum(testVec[i][0])

	n2 = FactNum.DigitNum(testVec[i][1])
	
	testEq = (n1 == n2)

	print n1, "==", n2 , " : " , testEq

	if testEq != resVec[i]:
		raise ValueError("Expected:", resVec[i], ", got:",testEq)

################################
# Testing inequality operator (__ne__)
################################

testVec = [ [122,122], [122,123], [222,122]]
resVec = [ False,True, True ]

print "-- Testing not equal operator:"
for i in range(len(testVec)):

	n1 = FactNum.DigitNum(testVec[i][0])

	n2 = FactNum.DigitNum(testVec[i][1])
	
	testNeq = (n1 != n2)

	print n1, "!=", n2 , " : " , testNeq

	if testNeq != resVec[i]:
		raise ValueError("Expected:", resVec[i], ", got:",testNeq)

################################
# Testing add operator
################################
testVec = [ [123,321], [123,7]]
resVec = [ 444,130 ]

print "-- Testing add operator:"
for i in range(len(testVec)):

	n1 = FactNum.DigitNum(testVec[i][0])

	n2 = FactNum.DigitNum(testVec[i][1])

	expAdd = FactNum.DigitNum(resVec[i])
	
	testAdd = n1 + n2

	print n1 , "+" , n2 , "=", testAdd

	if testAdd!=expAdd:
		raise ValueError("Expected:", expAdd ,", got:", N)

################################
# Testing multipliying operator
################################
testVec = [ [2,7,14], [11,10,110], [99,22,2178]]

print "-- Testing multiply operator:"
for i in range(len(testVec)):

	n1 = FactNum.DigitNum(testVec[i][0])

	n2 = FactNum.DigitNum(testVec[i][1])

	expMul = FactNum.DigitNum(testVec[i][2])

	testMul = n1*n2

	print n1 , "*" , n2 , "=", testMul

	if testMul != expMul:
		raise ValueError("Expected:", expMul," , got:",testMul)

