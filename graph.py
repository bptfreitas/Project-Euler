import sys

class Graph:

	def __init__(self,graph):
		self.__graph = graph 
		self.__shortest_dists = {} 
		self.__longest_dists = {} 

	def __getitem__(self,key):
		return self.__graph[key][0]

	def __setitem__(self,key,value):
		self.__graph[key][0]=value

	def __repr__(self):
		string = ''
		for vertex_src in self.__graph.keys():
			for vertex_dst,weight in self.__graph[vertex_src][1:]:
				string+= "(" + str(vertex_src) + ") [" + str(self.__graph[vertex_src][0]) + "]"
				string+= "--" + str(weight) + "--> " 
				string+= "(" + str(vertex_dst) + ") [" + str(self.__graph[vertex_dst][0]) + "]\n"

		return string

	def get_edges(self):
		edges = {  }
		for vertex_src in self.__graph.keys():
			for (vertex_dst,weight) in self.__graph[vertex_src][1:]:
				edges[vertex_src,vertex_dst]=weight

		return edges

	def get_vertexes(self):
		return { v : self.__graph[v][0] for v in self.__graph.keys() }

	def get_shortest_dists(self):
		return self.__shortest_dists

	def get_longest_dists(self):
		return self.__longest_dists

	# implements Dijkistra's shortest path algorithm
	def Dijkistra(self,start=[]):

		edges = self.get_edges()
		vertexes = self.get_vertexes()

		minQ = { vertex : sys.maxint for vertex in vertexes.keys() }
		pred= { vertex : -1 for vertex in vertexes.keys() }

		if start == []:
			start = sorted(vertexes.keys())[0]
	
		pred[start]=-1
		minQ[start]=0

		Dij = {}

		del self.__shortest_dists
		self.__shortest_dists = {}

		while (len(minQ)>0):
			U = min(minQ.iteritems(),key=lambda k: k[1])[0]

			#print "Chose: ", U
			for (u,v) in [ e for e in edges.keys() if e[0]==U and e[1] in minQ.keys() ]:
				w = edges[u,v]
				if minQ[v]>minQ[u]+w:
					#print "(",u,",",v,"): ", minQ[v], " -> ", minQ[u]+w
					minQ[v]=minQ[u]+w
					pred[v]=u

			Dij[U]=[vertexes[U]]
			if pred[U]!=-1:
				Dij[pred[U]].append([ U, edges[pred[U],U] ])

			self.__shortest_dists[U]=minQ[U]

			del minQ[U]

		return Graph(Dij)

	# implements Bellman Ford shortest path algorithm
	def BellmanFord(self,start=0,minmax = 'min' ):

		edges = self.get_edges() 
		vertexes = self.get_vertexes()

		dist = { vertex : sys.maxint if minmax=='min' else -sys.maxint-1 for vertex in vertexes.keys() }
		pred= { vertex : -1 for vertex in vertexes.keys() }
		
		pred[start]=-1
		dist[start]=0
	
		for counter in range(len(vertexes)):
			for (u,v),w in edges.iteritems():
				#print "(",u,",",v,"): ", dist[v], " -> ", dist[u]+w
				if minmax=='min' and dist[v]>dist[u]+w:
					dist[v]=dist[u]+w
					pred[v]=u
				elif minmax=='max' and dist[v]<dist[u]+w:
					dist[v]=dist[u]+w
					pred[v]=u

		if minmax=='min':
			self.__shortest_dists = dist
		elif minmax=='max':
			self.__longest_dists = dist
		
		BF = { v : [value] for v,value in vertexes.iteritems() }
		for v in vertexes.keys():
			if pred[v]!=-1:
				BF[pred[v]].append([v, edges[pred[v],v] ])
		
		return Graph(BF)


	#Implements Prim's algorithm for Minimum Spam Tree
	#vertexes: list of vertexes, as (id,value)
	#edges: list of edges, on the form (u,v,weight)
	def MST(self,start):
		minQ = { vertex : sys.maxint for vertex in vertexes.keys() }
		predQ = { vertex : -1 for vertex in vertexes.keys() }

		edges = self.get_edges()
		edges.sort(key = lambda x: x[2])
	
		print "minQ:\n", minQ
		print "predQ:\n",edges

		MST = {}

		minQ[start]=0

		while len(minQ)>0:
			U = min(minQ.iteritems(),key= lambda k: k[1] )[0]

			for (u,v,w) in [ e for e in edges if e[0]==U and e[1] in minQ.keys() ]:
				if w<minQ[v] and predQ[v]==-1:
					minQ[v]=w
					predQ[v]=u

			MST[U]=[vertexes[U]]
			if predQ[U]!=-1:
				MST[predQ[U]].append([ U,minQ[U] ])
				#MST[U].append([ predQ[U],minQ[U] ])

			del minQ[U]

		# building graph
		
		return MST




def test_MST():
	all_graphs = []
	graph1 = { }
	
	graph1["A"]=[["vertexA"],["C",5],["E",10]]
	graph1["B"]=[["vertexB"],["B",3],["D",7]]
	graph1["C"]=[["vertexC"],["C",2],["E",5]]
	graph1["D"]=[["vertexD"],["A",3],["E",8]]
	graph1["E"]=[["vertexE"],["B",2]]

	all_graphs.append(graph1)

	graph2 = dict(graph1)

	graph2["A"].append(["D",3])

	all_graphs.append(graph2)

	for graph in all_graphs:
		edges = [  ]
		for vertex_src in graph.keys():
			for (vertex_dst,weight) in graph[vertex_src][1:]:
				edges.append([vertex_src,vertex_dst,weight])

		vertexes = { v : graph[v][0] for v in graph.keys() }

		print "Graph:"
		print graph

		print "Vertexes:"
		print vertexes
	
		print "Edges:"
		print edges

		MST(vertexes,edges,"A")

def test_Dijkistra():

	graph = {}
	graph[0]=[ ['v0'],[1,5],[2,2],[4,9] ]
	graph[1]=[ ['v1'],[2,0],[4,2] ]
	graph[2]=[ ['v2'],[1,1],[3,6],[4,4] ]
	graph[3]=[ ['v3'],[2,3] ]
	graph[4]=[ ['v4'],[3,2] ]

	print Dijkistra(graph,0)


def test_BellmanFord():

	graph = {}
	graph[0]=[ ['v0'],[1,-3] ]
	graph[1]=[ ['v1'],[2,1] ]
	graph[2]=[ ['v2'],[3,1] ]
	graph[3]=[ ['v3'],[4,1] ]
	graph[4]=[ ['v4'] ]

	print BellmanFord(graph,0)

	graph = {}
	graph[0]=[ ['v0'],[1,2],[2,3] ]
	graph[1]=[ ['v1'] ]
	graph[2]=[ ['v2'],[1,-2] ]

	print BellmanFord(graph,0)
