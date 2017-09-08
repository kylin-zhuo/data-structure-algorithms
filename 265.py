"""
265. Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        min1, min2 = (-1, 0), (-1, 0)
        nrow, ncol = len(costs), len(costs[0])
        
        for i in range(nrow):
            
            ti1, tmin1 = min1[0], float('inf')
            ti2, tmin2 = min2[0], float('inf')
            
            for j in range(ncol):
                
                if (j != min1[0]) or (ti1 == -1):
                    t = costs[i][j] + min1[1]
                else:
                    t = costs[i][j] + min2[1]
                    
                if t < tmin1: 
                    tmin2 = tmin1
                    tmin1 = t
                    ti2 = ti1
                    ti1 = j
                    
                elif t < tmin2:
                    tmin2 = t
                    ti2 = j
                    
            min1 = (ti1, tmin1)
            min2 = (ti2, tmin2)
        
        return min1[1]
            
            
                
            