# no-89: Gray Code

class Solution(object):
    
    # @classmethod
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
        	for j in range(len(res)-1,-1,-1):
        		res.append(res[j] + (1<<i))
        return res

s = Solution()
# print Solution.grayCode(3)
print s.grayCode(3)
