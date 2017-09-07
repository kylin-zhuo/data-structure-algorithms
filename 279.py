"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import numpy as np
from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Build a graph and search the shortest path from target value e.g. 12 to 0. 

        graph = {}
        for i in range(n,0,-1):
        	sqrts = np.array(range(1, int(np.sqrt(i)) + 1))
        	sqaures = sqrts * sqrts
        	graph[i] = np.array([i] * len(sqaures)) - sqaures

        q = deque([(n,0)])
        s = set([n])
        while q:
        	current = q.popleft()
        	num, depth = current
        	if num == 0:
        		return depth
        	for child in graph[num]:
        		if child not in s:
        			q.append((child, depth+1))
        			s.add(child)


s = Solution()
print s.numSquares(1)