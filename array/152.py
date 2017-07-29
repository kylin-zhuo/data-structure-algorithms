"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        zero = next((i for i, v in enumerate(nums) if v == 0), -1)
        
        if zero == -1:
        
            n = len(nums)
            pos, cum, neg = [nums[0] if nums[0] > 0 else None] + [0]*(n-1), [nums[0]] + [0]*(n-1), [nums[0] if nums[0] < 0 else None] + [0]*(n-1)
            for i in range(1, len(nums)):
                cum[i] = cum[i-1]*nums[i]
                pos[i] = (pos[i-1] * nums[i] if pos[i-1] else nums[i]) if nums[i] > 0 else (nums[i] * neg[i-1] if neg[i-1] else None)
                neg[i] = (neg[i-1] * nums[i] if neg[i-1] else None) if nums[i] > 0 else (nums[i] * pos[i-1] if pos[i-1] else nums[i])

            return max(max(pos), max(cum), max(neg))
        else:
            return max(self.maxProduct(nums[:zero]), self.maxProduct(nums[zero+1:]), 0)