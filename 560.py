class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {nums[0]: 1}
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        cnt = dic.get(k, 0)        
        for n in nums:
            dic[n] -= 1
            cnt += dic.get(k + n, 0)
        
        return cnt