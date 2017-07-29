"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):

	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
# 		res = 0
# 		dic = dict()
# 		for n in nums:

# 			if n not in dic:
# 				left = dic[n-1] if (n-1) in dic else 0
# 				right = dic[n+1] if (n+1) in dic else 0
# 				s = left + right + 1
# 				dic[n] = s
# 				res = max(res, s)
# 				dic[n-left] = s
# 				dic[n+right] = s

# 		return res

		nums = set(nums)
		best = 0
		for x in nums:
			if x - 1 not in nums:
				y = x + 1
				while y in nums:
					y += 1
				best = max(best, y - x)
		return best