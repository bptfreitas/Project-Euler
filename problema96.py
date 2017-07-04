#!/usr/bin/time /usr/bin/python

#Su Doku

import argparse
import sys

from euler import get_primes2,binary_search,fact

from itertools import izip,combinations,product

from bisect import insort_left,insort

from math import log


class SudokuSolver:
	sudoku = []

	def __init__(self,matrix):
		self.sudoku = matrix;

	def __getitem__(self,key):
		x = key[0]
		y = key[1]
		if type(x)!=int or type(y)!=int:
			raise AttributeError

		if x not in set(range(10)) or y not in set(range(10)):
			raise IndexError

		return self.sudoku[x][y]

	def __setitem__(self,key,value):
		x = key[0]
		y = key[1]
		if type(x)!=int or type(y)!=int:
			raise AttributeError

		if ( x not in set(range(10)) ) or ( y not in set(range(10)) ):
			raise IndexError

		if value not in set(range(10)):
			raise ValueError

		self.sudoku[x][y]=value

	def __repr__(self):
		string = ""
		for x in xrange(9):
			if x%3==0:
				string += ''.join([ "-" for s in xrange(90) ])
				string +='\n'
			for y in xrange(9):
				string+= str(self[x,y]) if self[x,y]!=0 else "*"
				if (y+1)%3==0:
					string+='\t|\t'
				else:
					string+= "\t"
			string+="\n"
		return string

	# searches a value on a said line
	def search_value_on_line(self,value,line):
		if line not in set(range(9)):
			raise IndexError

		if value not in set(range(1,10)):
			raise ValueError

		for y in xrange(9):
			if self[line,y]==value:
				return True
		return False

	# searches a value on a said column
	def search_value_on_col(self,value,col):
		if col not in set(range(9)):
			raise IndexError

		if value not in set(range(1,10)):
			raise ValueError

		for x in xrange(9):
			if self[x,col]==value:
				return True
		return False

	def search_value_on_block(self,value,bx,by):
		if bx not in set(range(3)):
			raise IndexError

		if by not in set(range(3)):
			raise IndexError

		if value not in set(range(1,10)):
			raise ValueError

		for (x,y) in product(range(bx*3,bx*3+3),range(by*3,by*3+3)):
			if self[x,y]==value:
				return True

		return False

		

	# returns a list of unique values that can be put into position (line,col)
	def find_uniques(self,line,col,debug=False):
		if line not in set(range(9)):
			raise IndexError

		if col not in set(range(9)):
			raise IndexError

		#eliminate values that appear already on col, line, or block
		uniques = []		
		for value in xrange(1,10):
			found_value = False	
			if debug:
				print "value=",value
			for z in xrange(9):
				if debug:
					print "\t", (z,col), "\t", (line,z)
				if self[z,col]==value or self[line,z]==value:
					found_value=True
					break

			if found_value:
				continue

			block_col = col//3
			block_line = line//3

			for (x,y) in product(range(block_line*3,block_line*3+3),range(block_col*3,block_col*3+3)):
				if debug:
					print "\t\t", (x,y), "=", self[x,y]
				if self[x,y]==value:
					found_value=True
					break

			if found_value:
				continue

			uniques.append(value)
		
		return uniques

	def has_open_spots(self):
		for (x,y) in product(range(9),repeat=2):
			if self[x,y]==0:
				return True				
		return False

	def validade_line(self,line):
		if line not in set(range(9)):
			raise IndexError

		digits = range(1,10)
		for y in xrange(9):
			if self[line,y]!=0:
				try:
					digits.remove(self[line,y]);
				except:
					return False

		return True

	def validade_col(self,col):
		if col not in set(range(9)):
			raise IndexError

		digits = range(1,10)
		for x in xrange(9):
			if self[x,col]!=0:
				try:
					digits.remove(self[x,col]);
				except:
					return False

		return True

	def validade_block(self,block_line,block_col):
		if block_line not in set(range(3)):
			raise IndexError

		if block_col not in set(range(3)):
			raise IndexError

		digits = range(1,10)
		for (x,y) in product(range(block_line*3,block_line*3+3),range(block_col*3,block_col*3+3)):
			#print "\t(",x,",",y , ")"
			if self[x,y]!=0:
				try:
					digits.remove(self[x,y]);
				except:
					return False
		return True

	def fill_unique_spots(self):
		added_value=True
		while added_value:
			added_value=False

			for (x,y) in product(range(9),repeat=2):
				if sudoku[x,y]==0:
					uniques = self.find_uniques(x,y)
					#print (x,y) , "=" , uniques 
					if len(uniques) == 1:
						self[x,y]=uniques[0]
						added_value=True
					else:
						block_line = x//3
						block_col = y//3	

						uniques2 = []
						for u in uniques:
							check_lines=check_col=False

							if x==3*block_line:
								check_lines=self.search_value_on_line(u,x+1) and self.search_value_on_line(u,x+2)
							elif x==3*block_line+1:
								check_lines=self.search_value_on_line(u,x-1) and self.search_value_on_line(u,x+1)
							elif x==3*block_line+2:
								check_lines=self.search_value_on_line(u,x-1) and self.search_value_on_line(u,x-2)
							else:
								raise Exception("THIS CANNOT BE!!!")
						
							if y==3*block_col:
								check_col=self.search_value_on_col(u,y+1) and self.search_value_on_col(u,y+2)
							elif y==3*block_col+1:
								check_col=self.search_value_on_col(u,y-1) and self.search_value_on_col(u,y+1)
							elif y==3*block_col+2:
								check_col=self.search_value_on_col(u,y-1) and self.search_value_on_col(u,y-2)
							else:
								raise Exception("FEAR NO DARKNESS!")

							if check_lines and check_col:
								uniques2.append(u)

						if len(uniques2)==1:
							self[x,y]=uniques2[0]
							added_value=True
						elif len(uniques2)>0:
							raise Exception("OH GOD WHY HAVE YOU FORSAKEN ME!");

	def test_values(self,position,stack_unused,stack_used):

		#print stack_unused, stack_used
		valid_position = False
		
		while len(stack_unused)>0:

			value = stack_unused[len(stack_unused)-1]			

			self[position]=value
				
			test_line = self.validade_line(position[0])
			test_col = self.validade_col(position[1])
			test_block = self.validade_block(position[0]//3,position[1]//3)
			
			#print test_line, " ", test_col, " ", test_block

			valid_position = (test_line and test_col and test_block)

			if valid_position:
				break
			else:				
				stack_used.append(stack_unused.pop())				
	
		if not valid_position:
			self[position]=0
		
		return [stack_unused,stack_used]

	def depth_tree_search(self,open_spots={}):

		if open_spots == {}:
			open_spots = {}
			for (x,y) in product(range(9),repeat=2):
				if self[x,y]==0:
					open_spots[(x,y)]= self.find_uniques(x,y)

			#print [x for x in open_spots.iteritems() ]

			positions = open_spots.keys()
			positions.sort(key = lambda v: len(open_spots[v]))
			#print positions

			if len(positions)==0:
				return False

			pos = positions[0]
			values = open_spots[pos]			

			del open_spots[pos]

			for value in values:
				self[pos]=value
				#print pos, " - ", value
				#print self
				found = self.depth_tree_search(open_spots)
				if found:
					return True
		else:
			new_open_spots = dict(open_spots)
			positions = new_open_spots.keys()
			positions.sort()

			pos = positions[0]
			values = new_open_spots[pos]		

			del new_open_spots[pos]

			found = False

			for value in values:				
				self[pos]=value
				
				test_line 	= self.validade_line(pos[0])
				test_col 	= self.validade_col(pos[1])
				test_block 	= self.validade_block(pos[0]//3,pos[1]//3)

				if (test_line and test_col and test_block):		
					#print pos, " - ", value
					#print self
					if len(new_open_spots)==0:
						#print "SOLUTION FOUND"
						return True
					else:
						found = self.depth_tree_search(new_open_spots)
						if found:
							return True
				else:
					#print pos, " - ", value, " - can't, next value ..."					
					self[pos]=0
					#print self
				
			#print "all values for ", pos, " tested, going back on recursion"			
			self[pos]=0
			return False									
		
			
def test_SudokuSolver():
	################################
	#### Testing line validation ###
	################################

	test_lines = [ [ x+1 for x in xrange(9) ] for y in xrange(1,10) ]

	#1st line is all good: True
	#2nd line has 1 empty space at start: True
	test_lines[1][0]=-1
	#3rd line has 1 empty space at middle: True
	test_lines[2][5]=-1
	#4th line has 1 empty space at end: True
	test_lines[3][8]=-1
	#5th line has 1 repeating 2 times in a row: False
	test_lines[4][1]=1
	#6th line has 9 repeating 2 times in a row: False
	test_lines[5][7]=9
	
	sudoku = SudokuSolver(test_lines)

	print sudoku

	for line in xrange(9):
		print "Testing lines ", line , ": " , sudoku.validade_line(line)


	##################################
	#### Testing column validation ###
	##################################
	test_cols = [ [ y for x in xrange(9) ] for y in xrange(1,10) ]

	#1st column is all good: True
	#2nd column has 1 empty space at start: True
	test_cols[0][1]=-1
	#3rd line has 1 empty space at middle: True
	test_cols[5][2]=-1
	#4th line has 1 empty space at end: True
	test_cols[8][3]=-1
	#5th line has 1 repeating 2 times in a row: False
	test_cols[1][4]=1
	#6th line has 9 repeating 2 times in a row: False
	test_cols[7][5]=9


	sudoku = SudokuSolver(test_cols)
	print "Testing columns ... \n", sudoku

	for col in xrange(9):
		print "Testing column", col, ": " , sudoku.validade_col(col)

	#################################
	#### Testing block validation ###
	#################################
	test_blocks = [ [ (x%3+1)+(y%3)*3 for x in xrange(9) ] for y in xrange(9) ]

	#block (0,0) is all good: True
	#block (0,1) has 1 empty space at start: True
	test_blocks[0*3][1*3]=-1
	#block (0,2) has 1 empty space at middle: True
	test_blocks[0*3+1][2*3+1]=-1
	#block (1,0) has 1 empty space at end: True
	test_blocks[1*3+2][0*3+2]=-1
	#block (1,1) has 1 repeating 2 times in a row: False
	test_blocks[1*3][1*3+1]=1
	#block (1,2) has 9 repeating 2 times in a row: False
	test_blocks[1*3+2][2*3+1]=9

	sudoku = SudokuSolver(test_blocks)

	print "Testing blocks ... \n", sudoku

	for (x,y) in product(range(3),repeat=2):
		print "Testing block (", x, ",", y, ") : ", sudoku.validade_block(x,y)
				
	#################################
	#### Testing block validation ###
	#################################
	test_uniques = [ [ (x%3+1)+(y%3)*3 for x in xrange(9) ] for y in xrange(9) ]

	sudoku = SudokuSolver(test_uniques)

	for (x,y) in [ (x,y) for x in range(1,3) for y in range(3) ]:
		sudoku[x,y] = 0

	print "Testing unique value searching: \n", sudoku
	
	print sudoku.find_uniques(0,1)



with open("p096_sudoku.txt","r") as games:

	n=soma=0
	while n<5:
		name=games.readline()	
		if name is '':
			break

		sudoku_table=[]
		for x in range(9):
			line=games.readline()
			sudoku_line = [ int(line[i]) for i in xrange(9) ]
			sudoku_table.append(sudoku_line)

		sudoku = SudokuSolver(sudoku_table)

		print name, "\n", sudoku

		sudoku.fill_unique_spots()

		sudoku.depth_tree_search()

		soma += sudoku[0,0]*100+sudoku[0,1]*10+sudoku[0,2]

		print name[:len(name)-1], " - Solution \n" , sudoku		
		n+=1

	print soma
