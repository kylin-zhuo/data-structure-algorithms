### Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given `n = 5` and `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`, return true.

Given `n = 5` and `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`, return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, ``[0, 1]`` is the same as ``[1, 0]`` and thus will not appear together in edges.∏

------
Needs to return whether the graph is a tree and thus it is a union-find problem. Let the vertices be formed by themselves their own group initially, along with adding the edges onto the vertices one by one, check whether an edge is put between two vertices that have been assigned to the same parent.


| node | P(init)|p([0,1])|p([1,2])|p([2,3])
| :------ | :---- |:-|:-|:-|
| 0       | 0     |0| 0|0|
| 1       | 1     |0| 0|0|
| 2       | 2     |2| 0|0|
| 3       | 3     |3| 3|0|
| 4       | 4     |4| 4|4|

As the table shows, after adding edges ``[0,1], [1,2], [2,3]``, the node 0,1,2,3 all have the same parent 0. At the following edge ``[1,3]`` the algorithm will detect that vertex 1 and 3 have the same parent, so it will return `False`.

The addition: the number of connected components should be also considered. If there are more than one connected components, it will not be treated as a tree. Will use DFS to handle it.

**The python code:**

```
def validTree(edges, n):

    parents = range(n)

    def find(i):
        while parents[i] != i:
            i = parents[i]
        return i

    def union(i, j):
        pi, pj = find(i), find(j)
        parents[pj] = pi

    dic = defaultdict(set)

    for v1, v2 in edges:
        dic[v1].add(v2)
        dic[v2].add(v1)

    visited = set()

    def dfs(i):
        visited.add(i)
        for n in dic[i]:
            if n not in visited:
                dfs(n)

    dfs(0)
    if len(visited) < n:
    # if it is not the only one connected component
        return False

    for v1, v2 in edges:
        if find(v1) == find(v2):
            return False
        union(v1, v2)

    return True
```
