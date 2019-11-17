"""
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. 
The i-th edge connects nodes edges[i][0] and edges[i][1] together. 
Your task is to augment this set of edges with additional edges to connect all the nodes. 
Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

    n, an int representing the total number of nodes.
    edges, a list of integer pair representing the nodes already connected by an edge.
    newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively 
    (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).

Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.

"""

class Solution(object):
    
    def minimumCost(self, n, edges, newEdges):
        
        # initiate the disjoint set
        uf = UnionFind(n)
        
        # union the connected components
        for i, j in edges:
            uf.union(i, j)
        
        # sort the new edges:
        newEdges.sort(key = lambda x: x[2])

        cost = 0
        
        for f, t, val in newEdges:
            rf = uf.find(f)
            rt = uf.find(t)
            if rf == rt:
                continue
            cost += val
            uf.union(f, t)
            if uf.count == 1:
                break
        
        if uf.count > 1:
            print("impossible to finish.")

        return cost
        


class UnionFind(object):
    
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return 
        print("union", i, j)
        if self.rank[i] < self.rank[j]:
            self.parent[ri] = rj
        elif self.rank[i] > self.rank[j]:
            self.parent[rj] = ri
        else:
            self.parent[ri] = rj
            self.rank[ri] += 1
        self.count -= 1



if __name__ == "__main__":
    n = 6
    edges = [[1, 4], [4, 5], [2, 3]]
    newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    s = Solution()
    print(s.minimumCost(n, edges, newEdges))

