class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        lnums = len(nums)
        res = 9223372036854775807

        for i in range(lnums-2):

            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                remain = target - nums[i]
                lo, hi = i + 1, len(nums) - 1
                while lo < hi:
                    if abs(nums[lo] + nums[hi] - remain) < res:
                        res = abs(nums[lo] + nums[hi] - remain)
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1

        return res



test = [-1, 0, 1, 2, -1, -4]
s = Solution()
print s.threeSumClosest(test, 3) 


