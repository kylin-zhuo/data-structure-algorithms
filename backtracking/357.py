"""
No.357 Count numbers with unique digits 

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, 
excluding [11,22,33,44,55,66,77,88,99])

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.

"""

class Solution(object):
	
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        used = [False for _ in range(10)]
        return self.helper(n, used, 0)
        
    def helper(self, n, used, d):
        if d == n: return 1
        count = 1
        start = 1 if d == 0 else 0
        for i in range(start, 10):
            if not used[i]:
                used[i] = True
                count += self.helper(n, used, d+1)
                used[i] = False
            
        return count