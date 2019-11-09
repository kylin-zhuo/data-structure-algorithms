import random

def partition(nums, p, r):

	indx = random.randint(p, r)

	nums[r], nums[indx] = nums[indx], nums[r]
	x = nums[r]
	i = p - 1

	for j in range(p, r):
		if nums[j] <= x:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]

	nums[i+1], nums[r] = nums[r], nums[i+1]
	return i+1


def quickSelect(nums, k):

	pos = partition(nums, 0, len(nums)-1)
	if pos > k:
		return quickSelect(nums[:pos], k)
	elif pos < k:
		return nums[:pos] + quickSelect(nums[pos:], k-pos)
	else:
		return nums[:pos]



nums = [5,2,7,6,1,8,9,3,4]

print quickSelect(nums, 4)
