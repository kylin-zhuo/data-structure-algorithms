def longestConsecutive(nums):

	s = set(nums)
	maxv = 0
	for n in nums:
		if n-1 not in s:
			cnt = 0
			while n in s:
				cnt += 1
				n += 1
			maxv = max(maxv, cnt)
	return maxv

nums = [100, 4, 200, 1, 3, 2]
print longestConsecutive(nums)

