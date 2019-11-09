def nearestSmallerElementsOnLeft(nums):

	stack = [nums[0]]
	res = ['_'] * len(nums)
	for i in range(1, len(nums)):
		if nums[i] > stack[-1]:
			res[i] = stack[-1]
		else:
			while stack and stack[-1] >= nums[i]:
				stack.pop()
			if stack:
				res[i] = stack[-1]
		stack.append(nums[i])
	return res

nums = [1, 3, 0, 2, 5, 4]
print nearestSmallerElementsOnLeft(nums)