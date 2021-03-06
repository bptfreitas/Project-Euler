#!/usr/bin/python

#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import math
import euler
import itertools

from euler import get_primes2
from euler import binary_search
from itertools import product
from operator import xor

import sys
import argparse
import string

parser = argparse.ArgumentParser(description='Decrypts some XOR text')

parser.add_argument('--dict',nargs='?',type=argparse.FileType('r'))
parser.add_argument('--file',nargs='?',type=argparse.FileType('r'))

args = parser.parse_args()


try:
	str_words = args.dict.readline()
except Exception:
	parser.print_usage()
	sys.exit(-1)
else:	
	words = str_words.translate(None,'"').lower().split(',')
	words.sort()
	print words

try:
	str_text = args.file.readline()
	text = [ int(t) for t in str_text.split(',') ]
except Exception:
	parser.print_usage()
	sys.exit(-2)

maximum=0
for key in product(string.ascii_lowercase,repeat=3):

	ascii_key = [ ord(x) for x in key ]

	decoded_text = ''.join([ chr(xor(ascii_key[i%3],int(text[i]))) for i in xrange(len(text)) ])

	counter = 0
	for word in words:
		counter+=decoded_text.count(word)

	if counter>maximum:
		maximum = counter
		total_ascii_sum = sum( [ord(char) for char in decoded_text] )

		print key, ":", decoded_text, "\nTotal ASCII Sum: ", total_ascii_sum



	


