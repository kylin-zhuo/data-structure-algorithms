# Detect cycle in an undirected graph
 
from collections import defaultdict
  
# Represents a undirected graph using adjacent list representation
class Graph:
  
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
        self.neighbors[v2].append(v1) 
  
    # A recursive function using visited and parent to detect cycle in subgraph starting from v.
    def visit(self, v, visited, parent):
        visited.add(v)
        # Recur for all the vertices adjacent to this vertex
        for n in self.neighbors[v]:
            # If the node is not visited then recurse on it
            if n not in visited: 
                if self.visit(n, visited, v):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, then there is a cycle
            elif parent != n:
                return True
        return False
         
  
    #Returns true if the graph contains a cycle, else false.
    def isCyclic(self):
        # Mark all the vertices as not visited
        visited = set()
        #DFS trees
        for node in self.nodes:
            if node not in visited: 
                if(self.visit(node, visited, -1)) == True:
                    return True
        return False


if __name__ == '__main__':

    nodes = ('A', 'B', 'C', 'D')
    edges = (('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'))

    graph = Graph(len(nodes))
    graph.addNodes(nodes)
    graph.addEdges(edges)

    print graph.neighbors
    print graph.nodes
    print graph.isCyclic()



