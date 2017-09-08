"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        nrow, ncol = len(s1), len(s2)
        res = [[None for _ in range(ncol+1)] for _ in range(nrow+1)]
        res[0][0] = True
        
        for i in range(1, nrow+1):
            res[i][0] = res[i-1][0] and (s1[i-1] == s3[i-1])
            
        for j in range(1, ncol+1):
            res[0][j] = res[0][j-1] and (s2[j-1] == s3[j-1])
        
        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                bool1 = res[i-1][j] and (s1[i-1] == s3[i+j-1])
                bool2 = res[i][j-1] and (s2[j-1] == s3[i+j-1])
                res[i][j] = (bool1 or bool2)
                
        return res[nrow][ncol]
        