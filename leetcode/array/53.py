"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
	def maxSubArray(self, nums):

		"""
		if not nums: return 0
		if len(nums) == 1: return nums[0]

		thesum = 0
		themax = 0

		for j in range(len(nums)):

			if nums[j] >= 0: 
				if thesum < 0:
					if nums[j] > themax: 
						themax = nums[j]
					thesum = nums[j]
				else: 
					thesum = thesum + nums[j]
			else:
				thesum = thesum + nums[j]

			if thesum > themax:
				themax = thesum
		
		return themax
		"""

		# Dynamic programming

		res = [nums[0]]

		for i in range(1,len(nums)):
			res.append(max(res[i-1]+nums[i], nums[i]))
		return max(res)



s = Solution()
nums = [-2,-1]

print s.maxSubArray(nums)
