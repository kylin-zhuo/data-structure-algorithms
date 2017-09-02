"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0
        
        i = j = tmp_sum = 0
        minv = float('inf')
        
        while j < len(nums):
            tmp_sum += nums[j]
            j += 1    
            while tmp_sum >= s:
                minv = min(minv, j - i)
                tmp_sum -= nums[i]
                i += 1
                
        return 0 if minv == float('inf') else minv