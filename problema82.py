#!/usr/bin/python

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

import argparse
import random
import sys

from euler import get_primes2,binary_search,fact

from itertools import izip,combinations,product

from bisect import insort_left,insort
	
from math import log

from graph import Graph

RIGHT	= (0,1)
DOWN	= (1,0)	
UP		= (0,-1)
LEFT	= (-1,0)

dirnames = { (0,1) : "R" ,  (0,-1) : "L" , (-1,0): "U" , (1,0) : "D" }

def find_min(matrix,output,x,y,history=[sys.maxint,[]],Sum=0,verbose=False):
	#print "Visiting Node: ", (x,y)
	if x==len(matrix)-1 and y==len(matrix[x])-1:		
		if Sum+matrix[x][y]<history[0]:
			history[0]=Sum+matrix[x][y]
			output.write("New minimum sum found: "+ str(history[0]) +"\n")
			output.flush()
			return Sum+matrix[x][y]
		else:
			return history[0]
	else:
		directions = []
		if y%2==0:
			directions = [RIGHT,DOWN]
		else:
			directions = [DOWN,RIGHT]
		
		minimum = 0		
		for (xi,yi) in directions:
			xn = x + xi
			yn = y + yi
			history[1].append(dirnames[(xi,yi)])
			if (Sum+matrix[x][y])<history[0] and (x+xi)<len(matrix) and (y+yi)<len(matrix[0]) :
				find_min(matrix,output,xn,yn,history,Sum+matrix[x][y],verbose)
			elif verbose and (x+xi)<len(matrix) and (y+yi)<len(matrix[0]):
				output.write("Pruning path: " + str(Sum+matrix[x][y]) + ">" + str(history[0]) + " (length: "+str(len(history[1]))+")\n")
				output.write("\t" + '->'.join(history[1]) + " with " + dirnames[(xi,yi)] +'\n')
			elif verbose:
				output.write("Limit reached\n")

			history[1].pop()
		return history[0]
				

def find_min2(matrix,x,y,record=sys.maxint,Sum=0):
	#print "Visiting Node: ", (x,y)
	if x==len(matrix)-1 and y==len(matrix[x])-1:
		return Sum+matrix[x][y]
	elif x==len(matrix) or y==len(matrix[x]):
		return sys.maxint
	else:
		directions = [RIGHT,DOWN]

		directions = filter(lambda key: (key[0]+x)<len(matrix) and (key[1]+y)<len(matrix[x]) ,directions)

		directions.sort(key = lambda k: (matrix[x+k[0]][y+k[1]]-matrix[x][y]),reverse=True)

		#print directions
		
		for (xi,yi) in directions:
			xn = x + xi
			yn = y + yi
			if (Sum+matrix[x][y])<record:
				subtree_sum = find_min2(matrix,xn,yn,record,Sum+matrix[x][y])

				if subtree_sum < record:
					record = subtree_sum
			#else:
			#	print "\tKilling subtree"

		return record

def find_min_sum(graph,node,end_node,visited=[]):
	if node==end_node:
		return [graph[node][0],True]
	else:		
		for child in graph[node][1:]:
			if child[0]!=node and child[0] not in visited:
				ret = find_min_sum(graph,child[0],end_node,visited+[child[0]])
				if ret[1]==True:
					return [graph[node][0]+ret[0],True]
		return [0,False]

		
def matrix2graph(matrix):
	nr_rows = len(matrix)
	nr_cols = len(matrix[0])
	
	graph = { x*nr_cols+y : [ [matrix[x][y]] ] for (x,y) in product(xrange(nr_rows),xrange(nr_cols)) }
	for (x,y) in product(xrange(nr_rows),xrange(nr_cols)):
		vertex = x*nr_cols+y

		if x<nr_rows and (y+1)<nr_cols:
			vertex_right = x*nr_cols+(y+1)
			
			graph[vertex].append([vertex_right,matrix[x][y+1]])

		if (x+1)<nr_rows and y<nr_cols:
			vertex_down = (x+1)*nr_cols+y

			graph[vertex].append([vertex_down,matrix[x+1][y]])

		if (x-1)>=0 and y<nr_cols:
			vertex_up = (x-1)*nr_cols+y

			graph[vertex].append([vertex_up,matrix[x-1][y]])

	return graph


parser = argparse.ArgumentParser(description='Takes a nxn matrix read from standard input and finds the path from top left to lower right with minimum sum of values')

parser.add_argument('--input', nargs='?',type=argparse.FileType('r'),default=sys.stdin,
	help="Input mxn integer matrix. Values must be comma-separated. Each line equals a matrix line")

parser.add_argument('--output', nargs='?',type=argparse.FileType('w'),default=sys.stdout,
	help="Output file")

parser.add_argument('--verbose', action = 'store_true', help="Prints program's verbose output")

args = parser.parse_args()

line_nr = 0
matrix=[]
while True:	
	try:
		line=args.input.readline()
		if line.strip()=='':
			break
		matrix_line = [ int(value) for value in line.split(',') ]
	except IndexError:
		msg = "Incorrect number of columns on line "+str(line_nr)+" (must have 9 columns)"
		sys.stderr.write("Error: " + msg + "\n")
		sys.exit(-1)
	except ValueError:
		msg = "Invalid value for a column detected on line " + str(line_nr)
		sys.stderr.write("Error: " + msg + "\n")
		sys.exit(-1)
	else:
		matrix.append(matrix_line)
		line_nr+=1

for line in range(len(matrix)-1):
	if len(matrix[line])!=len(matrix[line+1]):
		msg = "Line " + str(line) + " doesn't have the same number of elements of line " + str(line+1)
		sys.stderr.write("Error: " + msg + "\n")
		sys.exit(-1)
										
args.output.write("Finding minimum sum path for matrix ... \n")

g = matrix2graph(matrix)
graph = Graph(g)

#print graph

end_nodes = range(len(matrix)-1,len(matrix)**2,len(matrix))
#print end_nodes
minimum_list = []

for start_node in range(0,len(matrix)**2,len(matrix)):

	graph.Dijkistra(start = start_node)

	distances = graph.get_shortest_dists()
			
	result = graph[start_node][0]+min( [ distances[n] for n in end_nodes ] )

	minimum_list.append(result)

	args.output.write("Starting at "+ str(start_node) + " = "+str(result)+"\n")

args.output.write("Minimum sum: "+ str(min(minimum_list))+"\n")
