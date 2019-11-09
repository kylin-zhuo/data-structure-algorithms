class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        
        i, j, k = 0, 0, len(nums)
        # nums[:i] are 0, nums[i:j] are 1, nums[j:k] are not detected, nums[k:] are 2
        
        while j < k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            j += 1
