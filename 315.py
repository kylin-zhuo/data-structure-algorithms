class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 5,2,6,1


    def mergesort(self, nums, low, high, ans):
    	if low + 1 == high:
    		return
    	mid = (low + high) / 2
    	right = mid

    	self.mergesort(nums, low, mid, ans)
    	self.mergesort(nums, mid, high, ans)

    	for i in range(low, mid):
    		while right < high and nums[i][1] > nums[right][1]:
    			rignt += 1
    		ans[nums[i][0]] += right - mid
    	