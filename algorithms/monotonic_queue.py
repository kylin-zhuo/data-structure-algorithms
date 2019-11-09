# from leetcode 239 - Sliding Window Maximum

from collections import deque

class Monoqueue:

	m_deque = deque()
	# the m_deque stores the 2-length list
	# with the first element: the actual value
	# the second element: how many elements were deleted between itself and the one before it.

	def push(self, val):
		count = 0
		while self.m_deque and self.m_deque[-1][0] < val:
			count += self.m_deque[-1][1] + 1
			# self.m_deque.popright() -- no 'popright' method lol ><
			self.m_deque.pop()

		self.m_deque.append([val, count])

	def max(self):
		return self.m_deque[0][0]

	def pop(self):
		if self.m_deque[0][1] > 0:
			self.m_deque[0][1] -= 1
			return 
		self.m_deque.popleft()


k = 3
nums = [1,3,-1,-3,5,3,6,7]
mq = Monoqueue()

for i in range(k-1):
	mq.push(nums[i])

i = k - 1

while i < len(nums):
	mq.push(nums[i])
	print mq.max()
	mq.pop()
	i += 1


