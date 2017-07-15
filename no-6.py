class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
        	return s
        	
        indx = [[] for i in range(numRows)]
        for i in range(len(s)):
        	indx[self.process(i, numRows)].append(s[i])
        res = ''
        for i in range(numRows):
        	res += self.transform(indx[i])

        return res


    def process(self, i, numRows):
    	x = i % (2*numRows - 2)
    	return x if x < numRows else 2*numRows - 2 - x

    def transform(self, s):
    	res = ''
    	for i in range(len(s)): res += s[i]
    	return res


test = 'A'
s = Solution()
print s.convert(test, 1)