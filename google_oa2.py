import bisect

class TreeNode(object):
	def __init__(self, minv, maxv):
		self.minv = minv
		self.maxv = maxv
		self.left = None
		self.right = None


class Solution(object):

	def prune(self, root):
		while True:
			if (root.left and root.right) or (not root.left and not root.right):
				break
			root = root.left if root.left else root.right

	def solution1(self, nums, k):

		s = len(nums)
		root = TreeNode(0, s+1)

		for day, elem in enumerate(nums):

			cur = root

			flag = False
			while cur.left or cur.right:
				if cur.left and elem < cur.left.maxv:
					cur = cur.left
				elif cur.right and elem > cur.right.minv:
					cur = cur.right
				else:
					flag = True
					break

			if flag or elem < cur.minv or elem > cur.maxv:
				continue

			left_gap, right_gap = elem - cur.minv - 1, cur.maxv - elem - 1
			cur.left, cur.right = TreeNode(cur.minv, elem), TreeNode(elem, cur.maxv)

			if k in (left_gap, right_gap):
				return day + 1
			elif left_gap < k and right_gap < k:
				continue
			elif left_gap < k:
				cur.left = None

			elif right_gap < k:
				cur.right = None

			self.prune(root)

		return -1

	def solution2(self, nums, k):

		s = len(nums)
		res = [0, s]
		for i, val in enumerate(nums):
			pos = bisect.bisect_left(res, val)
			if res[pos] - val == k + 1 or val - res[pos-1] == k + 1:
				return i + 1
			res = res[:pos] + [val] + res[pos:]
			print i
		return -1


import random
nums = range(1,100000)
# random.shuffle(nums)
print Solution().solution2(nums, 9)

