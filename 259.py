"""
259. 3Sum Smaller
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        end, count = len(nums) - 1, 0
        
        def get_sum(i, j, k):
            return nums[i] + nums[j] + nums[k]
        
        for i in range(end-1):    
            j, k = i + 1, end
            while j < k:
                
                if get_sum(i,j,k) < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count

        