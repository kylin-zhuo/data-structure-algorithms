"""
219 Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i, d = 0, dict()
        for num in nums:
            if num in d and abs(d[num] - i) <= k: return True
            d[num] = i
            i += 1
        return False