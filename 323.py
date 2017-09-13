"""
323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.


"""

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # Firstly construct the Graph
        graph = {i: set() for i in xrange(n)}
        
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        seen = set()
        count = 0
        
        def bfs(node):
            queue = [node]
            for n in queue:
                for nei in graph[n]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
        
        for i in range(n):
            if i not in seen:
                bfs(i)
                count += 1
        
        return count
        
        
        
        
        