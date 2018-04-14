def subArraySum1(nums, target):
	# all are non-negative
	curr_sum = nums[0]
	n = len(nums)
	start = 0
	for i in range(1, n):

		while curr_sum > target and start < i-1:
			curr_sum -= nums[start]
			start += 1

		if curr_sum == target:
			print "Sum found between " + str(start) + " and " + str(i-1)
			return 1

		if i < n:
			curr_sum += nums[i]

	print "No subarray found"
	return 0

def subArraySum2(nums, target):
	# elements can be negative
	curr_sum = 0
	n = len(nums)
	dic = {}
	for i in range(n):
		curr_sum += nums[i]
		if curr_sum == target:
			print "Sum found between 0 to " + str(i)
			return 1
		if curr_sum - target in dic:
			print "Sum found between " + str(dic[curr_sum-target]+1) + " to " + str(i)
			return 1
		dic[curr_sum] = i
	print "No subarray found"
	return 0



nums1 = [15, 2, 4, 8, 9, 5, 10, 23]
subArraySum1(nums1, 23)

nums2 = [10, 2, -2, -20, 10]
subArraySum2(nums2, -12)
