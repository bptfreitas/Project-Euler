#!/usr/bin/python

import sys,argparse

from graph import Graph

MIN = True
MAX = False

def depth_sum(tree,depth,node,record=[sys.maxint],Sum=0):
	if depth== len(tree)-1:
		if Sum+tree[depth][node]>record[0]:
			record[0]=Sum+tree[depth][node]
		return record[0]
	else:
		# tests if we have to prune a branch
		if Sum+tree[depth][node]>record[0]:
			# branch left child
			left_child=depth_sum(tree,depth+1,node,record,Sum+tree[depth][node])

			# branch right child
			right_child=depth_sum(tree,depth+1,node+1,Sum+tree[depth][node])

		return record[0]


def matrix2graph(matrix):
	vertexes = {}
	base = 0
	for line in mat:
		for index,val in enumerate(line):
			vertexes[base+index]=(base,index)
		base+=len(line)

	graph = {}
	for depth in range(len(mat)):
		base = depth*(depth+1)/2
		for node in range(len(mat[depth])):
			graph[base+node]=[ [mat[depth][node]] ]

			if depth<len(mat)-1:			
				w1 = mat[depth+1][node]
				graph[base+node].append( [base+len(mat[depth])+node,w1] )

				w2 = mat[depth+1][node+1]
				graph[base+node].append( [base+len(mat[depth])+node+1,w2] )
				
	return graph
			

parser = argparse.ArgumentParser(description='Takes a nxn matrix read from standard input and finds the path from top left to lower right with minimum sum of values')

parser.add_argument('--input', nargs='?',type=argparse.FileType('r'),default=sys.stdin,
	help="Input mxn integer matrix. Each line equals a matrix line. Values must be comma-separated")

parser.add_argument('--output', nargs='?',type=argparse.FileType('w'),default=sys.stdout,
	help="Output file")

parser.add_argument('--prunepoint', nargs='?',type=int,default=sys.maxint,
	help="Starting prune value")

parser.add_argument('--verbose', action = 'store_true', help="Prints program's verbose output")

args = parser.parse_args()


nr_line = 0
nr_elems = 0
line_len = 1
with args.input as pyramid:

	mat=[]
	for line in pyramid:
		try:			
			mat_line=[ int(e) for e in line.split() ]
		except ValueError:
			msg = "Line " +str(nr_line)+" breaks pyramid formation"
			sys.stderr.write("Error: " + msg + "\n")
			sys.exit(-1)
		else:
			if len(mat_line)!=line_len:
				msg = "Expected "+str(line_len)+" elements on line " +str(nr_line)+", got " + str(len(mat_line))
				sys.stderr.write("Error: " + msg + "\n")
				sys.exit(-1)
			
			mat.append(mat_line)

			nr_elems+=len(mat_line)
			nr_line+=1
			line_len+=1

	g = matrix2graph(mat)
	graph = Graph(g)

	print graph

	print graph.BellmanFord(minmax='max')
		
	distances = graph.get_longest_dists()
	last_line = filter(lambda k: k>nr_elems-line_len,graph.get_longest_dists().keys())
	
	print last_line, len(last_line), line_len-1

	print max([ distances[k] for k in last_line ])+graph[0][0]
