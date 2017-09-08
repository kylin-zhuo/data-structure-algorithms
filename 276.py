"""
276. Paint Fence

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 1:
            return k if n == 1 else 0
        dif_last_two, same_last_two = [0, k, k*(k-1)] + [0] * (n-2), [0, k, k] + [0] * (n-2)

        for i in range(3, n+1):
            same_last_two[i] = dif_last_two[i-1]
            dif_last_two[i] = same_last_two[i-1] * (k-1) + dif_last_two[i-1] * (k-1)
            
        return same_last_two[-1] + dif_last_two[-1]