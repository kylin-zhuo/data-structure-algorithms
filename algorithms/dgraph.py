# the implemented directed graph
from collections import defaultdict

class DGraph:


    def __init__(self, n_vertices=0):
        self.V = n_vertices 
        # adjacent list
        self.neighbors = defaultdict(list)
        self.nodes = set()

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)
        self.V = len(self.nodes)

    def addNode(self, n):
        self.nodes.add(n)

    def addEdges(self, edges):
        for v1, v2 in edges:
            self.addEdge(v1, v2)
 
    def addEdge(self, v1, v2):
        self.neighbors[v1].append(v2) 


    def visit(self, v, visited, stack):
    	visited.add(v)
    	for n in self.neighbors[v]:
    		if n not in visited:
    			self.visit(n, visited, stack)
    	stack.append(v)

    def topological_sort(self):
    	visited = set([])
    	stack = []
    	for node in self.nodes:
    		if node not in visited:
    			self.visit(node, visited, stack)
    	return stack[::-1]


graph = DGraph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('B', 'E')]
nodes = ('A', 'B', 'C', 'D', 'E')

graph.addNodes(nodes)
graph.addEdges(edges)

print graph.topological_sort()

