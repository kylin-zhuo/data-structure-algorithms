"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible
"""

class Solution(object):
    
    def __init__(self):
        self.n = 0
        self.graph = {}
        
    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and adds to recursion stack
        visited.add(v)
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in recStack then graph is cyclic
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True

        # The node needs to be poped from the recursion stack before function ends
        recStack[v] = False
        return False

    
    def isCyclic(self):
        visited = set()
        recStack = [False] * self.n
        for node in range(self.n):
            if node not in visited:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # equivalent to the problem of detecting cycles in a directed graph
        self.n = numCourses
        self.graph = {x: set() for x in xrange(numCourses)}
        
        for course, pre in prerequisites:
            self.graph[pre].add(course)
        
        return not self.isCyclic()
