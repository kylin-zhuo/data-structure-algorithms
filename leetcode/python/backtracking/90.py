"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result, tmp = [], []
        self.helper(nums, tmp, result, 0)
        return result
        
    def helper(self, nums, tmp, result, start):
        result.append(list(tmp))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            new_tmp = list(tmp)
            new_tmp.append(nums[i])
            self.helper(nums, new_tmp, result, i+1)