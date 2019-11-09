"""
class Solution(object):
    def threeSum(self, nums):
        # :type nums: List[int]
        # :rtype: List[List[int]]


        nums = sorted(nums)
        i, k = 0, len(nums) - 1
        j = i+1

        res = []

        while True:

            tmp = nums[i] + nums[j] + nums[k]

            if i==j-1 and j==k-1: 
                if tmp == 0:
                    if [i,j,k] not in res: res.append([i,j,k])
                    break

            if tmp != 0:
                i,j,k = self.adjust_right(i,j,k) if tmp < 0 else self.adjust_left(i,j,k)

            else:
                if [nums[i],nums[j],nums[k]] not in res: res.append([nums[i],nums[j],nums[k]])
                if j < k - 1:
                    j += 1
                else:
                    j -= 1

        return res


    def adjust_right(self, i, j, k):

        if j < k - 1: return i, j+1, k
        else: return i+1, j, k

    def adjust_left(self, i, j, k):

        if j > i + 1: return i, j-1, k
        else: return i, j, k-1


if __name__ == '__main__':

    test = [-1, 0, 1, 2, -1, -4]
    # test = [-4, -1, -1, 0, 1, 2]

    s = Solution()
    return_res = s.threeSum(test)

"""


class Solution(object):

    def threeSum(self, nums):

        nums = sorted(nums)
        lnums = len(nums)
        res = []

        for i in range(lnums-2):

            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                target = 0 - nums[i]
                lo, hi = i + 1, len(nums) - 1
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1

        return res

test = [-1, 0, 1, 2, -1, -4]
s = Solution()
print s.threeSum(test) 









