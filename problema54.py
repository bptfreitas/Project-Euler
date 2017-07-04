#!/usr/bin/python

#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#    High Card: Highest value card.
#    One Pair: Two cards of the same value.
#    Two Pairs: Two different pairs.
#    Three of a Kind: Three cards of the same value.
#    Straight: All cards are consecutive values.
#    Flush: All cards of the same suit.
#    Full House: Three of a kind and a pair.
#    Four of a Kind: Four cards of the same value.
#    Straight Flush: All cards are consecutive values of same suit.
#    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:
#Hand	 	Player 1	 	Player 2	 	Winner
#1	 	5H 5C 6S 7S KD
#Pair of Fives
#	 	2C 3S 8S 8D TD
#Pair of Eights
#	 	Player 2
#2	 	5D 8C 9S JS AC
#Highest card Ace
#	 	2C 5C 7D 8S QH
#Highest card Queen
#	 	Player 1
#3	 	2D 9C AS AH AC
#Three Aces
#	 	3D 6D 7D TD QD
#Flush with Diamonds
#	 	Player 2
#4	 	4D 6S 9H QH QC
#Pair of Queens
#Highest card Nine
#	 	3D 6D 7H QD QS
#Pair of Queens
#Highest card Seven
#	 	Player 1
#5	 	2H 2D 4C 4D 4S
#Full House
#With Three Fours
#	 	3C 3D 3S 9S 9D
#Full House
#with Three Threes
#	 	Player 1

#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?


import euler

from math import sqrt
from euler import binary_search
from euler import is_prime
from euler import is_permutation
from euler import gen_pandigitals
from euler import get_primes2
from itertools import permutations
from itertools import combinations

def get_cards(hand):
	cards = {}
	for card in hand:
		valor = card[:len(card)-1]
		naipe = card[len(card)-1]
		if valor == 'T':
			valor = 10
		elif valor == 'J':
			valor = 11
		elif valor == 'Q':
			valor = 12
		elif valor == 'K':
			valor = 13
		elif valor == 'A':
			valor = 14
		else:
			valor = int(valor)

		if valor not in cards.keys():
			cards[valor]=[naipe]
		else:
			cards[valor].append(naipe)

	return cards

def get_game(hand,debug=True):

	cards = get_cards(hand)
			
	if debug:
		print hand, ": ", cards
		print [ cards[x][y] for x in cards.keys() for y in range(len(cards[x])) ]

	if sorted(cards.keys())==[10,11,12,13,14] and len(set(cards.values()[x][0] for x in range(5))) ==1:
		if debug:
			print "Royal Flush"
		return 100;
	elif sorted(cards.keys())==[ min(cards.keys()) +x for x in range(5) ] and len(set(cards.values()[x][0] for x in range(5))) ==1:
		if debug:
			print "Straight Flush"
		return 90;
	elif len(cards[cards.keys()[0]])==4 or len(cards[cards.keys()[1]])==4:
		if debug:
			print "Four-of-a-Kind"
		return 80;
	elif (len(cards[cards.keys()[0]])==3 and len(cards[cards.keys()[1]])==2) or (len(cards[cards.keys()[0]])==2 and len(cards[cards.keys()[1]])==3):
		if debug:
			print "Full-House"
		return 70;
	elif len(set([ cards[x][y] for x in cards.keys() for y in range(len(cards[x])) ])) ==1:
		if debug:
			print "Flush"
		return 60;
	elif sorted(cards.keys())==[ min(cards.keys())+x for x in range(5) ]:
		if debug:
			print "Straight"
		return 50;
	elif len(cards[cards.keys()[0]])==3 or len(cards[cards.keys()[1]])==3 or len(cards[cards.keys()[2]])==3:
		if debug:
			print "Three-of-a-Kind"
		return 40;
	elif sum ( [ 1 for x in range(len(cards)) if len(cards[cards.keys()[x]])==2 ] ) == 2:
		if debug:
			print "Two Pairs"
		return 30;
	elif sum ( [ 1 for x in range(len(cards)) if len(cards[cards.keys()[x]])==2 ] ) == 1:
		if debug:
			print "Pair"
		return 20;
	else:
		if debug:
			print "Highest card:", max(cards.keys())
		return max(cards.keys());

def test_get_game():
	print "Testing Royal Flush ... "
	royal_flush_games = [ ['JS','10S','AS','KS','QS'] ]
	for royal_flush in royal_flush_games:
		print get_game(royal_flush,debug=True)

	print "Testing Straight Flush ... "
	straight_flush_games = [ ['9S','10S','8S','7S','6S'] ]
	for straight_flush in straight_flush_games:
		print get_game(straight_flush,debug=True)

	print "Testing Four-of-a-Kind ... "
	four_games = [ ['9S','10S','9S','9S','9S'] ]
	for four in four_games:
		print get_game(four,debug=True)

	print "Testing Full-House ... "
	fullhouse_games = [ ['9S','10H','9S','9S','10D'] ]
	for fullhouse in fullhouse_games:
		print get_game(straight_flush,debug=True)

	print "Testing Flush ... "
	flush_games = [ ['1S','10S','3S','QS','KS'] ]
	flush_games.append( ['1D','10D','3D','QD','KD'] )
	for flush in flush_games:
		print get_game(flush,debug=True)

	print "Testing Three-of-a-Kind ... "
	three_games = [ ['1S','1S','3S','1S','KD'] ]
	three_games.append( ['1D','3D','3D','3D','KS'] )
	for three in three_games:
		print get_game(three,debug=True)

	print "Testing Two Pairs ... "
	twopair_games = [ ['1S','1S','3S','3S','2D'] ]
	twopair_games.append( ['4D','3D','3D','4D','KS'] )
	for twopair in twopair_games:
		print get_game(twopair,debug=True)

	print "Testing Single Pairs ... "
	twopair_games = [ ['1S','1S','4S','3S','2D'] ]
	twopair_games.append( ['4D','2D','3D','4D','KS'] )
	for twopair in twopair_games:
		print get_game(twopair,debug=True)

	print "Testing Highest card ... "
	highest_games = [ ['2S','7S','3S','10S','9D'] ]
	highest_games.append( ['4D','JD','QD','3D','KS'] )
	for highest in highest_games:
		print get_game(highest,debug=True)

def decide_winner(hand1,hand2,debug=False):

	game1 = get_game(hand1)
	game2 = get_game(hand2)

	if game1>game2:
		if debug:
			print "\t", 1
		return 1
	elif game2>game1:
		if debug:
			print "\t", 2
		return 2
	else:
		cards1 = get_cards(hand1)
		cards2 = get_cards(hand2)

		pairs1 = sorted([ (len(cards1[x]),x) for x in cards1.keys() ],key = lambda r:r[1], reverse=True)
		pairs1 = sorted(pairs1,key = lambda r : r[0], reverse=True)

		pairs2 = sorted([ (len(cards2[x]),x) for x in cards2.keys() ],key = lambda r:r[1], reverse=True)
		pairs2 = sorted(pairs2,key = lambda r : r[0], reverse=True)

		if debug:
			print "\t", pairs1
			print "\t", pairs2

		for i in range(len(pairs1) if len(pairs1)>len(pairs2) else len(pairs2)):
			if pairs1[i][1]>pairs2[i][1]:
				if debug:
					print "\t", 1
				return 1
			elif pairs1[i][1]<pairs2[i][1]:
				if debug:
					print "\t", 2
				return 2

		raise(ValueError, "OOOOOPS")

def test_decide_winner():	
	all_tests = [ [['5H','5C','6S','7S','KD'],['2C','3S','8S','8D','TD']] ]

	all_tests.append([['5D','8C','9S','JS','AC'],['2C','5C','7D','8S','QH']])

	all_tests.append([['2D','9C','AS','AH','AC'],['3D','6D','7D','TD','QD']])

	all_tests.append([['4D','6S','9H','QH','QC'],['3D','6D','7H','QD','QS']])

	all_tests.append([['2H','2D','4C','4D','4S'],['3C','3D','3S','9S','9D']])

	# deciding winner
	for test in all_tests:
		pair1 = test[0]
		pair2 = test[1]
		decide_winner(pair1,pair2,debug=True)

def problema54(filename='p054_poker.txt'):
	total = 0
	with open(filename,'r')	as arq_jogos:
		for jogo in arq_jogos:

			hands = jogo.strip('\n').split(' ')

			hand1 = hands[0:5]
			hand2 = hands[5:11]

			#print jogo, '\n', hand1, '\t' , hand2

			if decide_winner(hand1,hand2)==1:
				total+=1


		arq_jogos.close()

	print total

#test_decide_winner()

problema54()
