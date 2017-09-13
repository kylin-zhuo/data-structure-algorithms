"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # equivalent to the circle detection problem
        
        graph = {i: set() for i in xrange(n)}
        
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        seen = set()
        visited = set()
        
        def bfs(node):
            queue = [node]
            for v in queue:
                for nei in graph[v]:
                    if nei in visited:
                        continue
                    if nei in seen:
                        return False
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
                visited.add(v)
            return True if len(queue) == n else False
        
        return bfs(0)