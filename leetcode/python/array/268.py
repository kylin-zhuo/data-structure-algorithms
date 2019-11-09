class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        a = [0]*(len(nums)+1)
        for x in nums: a[x] = 1
        return a.index(0)
        """
        res,l = 0,len(nums)
        for x in range(l): res=res^x^nums[x]
        return res^l
