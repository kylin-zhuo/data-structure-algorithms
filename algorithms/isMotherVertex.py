# program to find a mother vertex in O(V+E) time
# the graph is directed graph

from collections import defaultdict
import itertools

class Graph:
 
    def __init__(self, edges):
        # edges format: ('A','B'), ('C','D'), ..
        vertices = set(itertools.chain(*edges))
        self.vertices = vertices
        self.V = len(vertices)
        self.graph = defaultdict(list) # default dictionary
        for v1, v2 in edges:
            self.graph[v1].append(v2)
 
    def dfs(self, v, visited):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfs(i, visited)

    def findMother(self):
 
        # Do the dfs on all the vertices of the graph
        visited = set()
        mother_cand = None
 
        for v in self.vertices:
            if v not in visited:
                self.dfs(v, visited)
                mother_cand = v

        # Check if the candidate is truely a mother node
        visited = set()
        self.dfs(mother_cand, visited)
        return mother_cand if len(visited) == self.V else -1

edges = [(0,1), (0,2), (1,3), (4,1), (6,4), (5,6), (5,2), (6,0)]
g = Graph(edges)

print g.findMother()