class UnionFind(object):
    def __init__(self, size):
        self.tree = list(range(size))

    def find(self, node):
        if self.tree[node] != node:
            self.tree[node] = self.find(self.tree[node])
        return self.tree[node]
        
    def union(self, x, y):
        self.tree[self.find(x)] = self.find(y)
    
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(1001)
        for e in edges:
            if uf.find(e[0]) == uf.find(e[1]):
                return e
            uf.union(e[0], e[1])
        return []