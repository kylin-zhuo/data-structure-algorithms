#11. Container With Most Water
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 1: return 0
        if len(height) == 2: return min(height[0], height[1])

        left, right = 0, len(height) - 1
        new_area, max_area = 0, min(height[right], height[0]) * right

        while left < right:
        	if height[left] < height[right]: left += 1
       		else: right -= 1
       		new_area = min(height[left], height[right]) * abs(right - left)
       		max_area = max(new_area, max_area)

       	return max_area

test = [1,2,3,4,5,6,7]

s = Solution()
print s.maxArea(test)