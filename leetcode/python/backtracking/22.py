class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        self.backtrack(res, "", 0, 0, n)

        return res

    def backtrack(self, res, current, nopen, nclose, n):

    	if len(current) == 2 * n: res.append(current)

    	if nopen < n: self.backtrack(res, current+'(', nopen+1, nclose, n)
    	if nclose < nopen: self.backtrack(res, current+')', nopen, nclose+1, n)


n = 3
s = Solution()
print s.generateParenthesis(n)