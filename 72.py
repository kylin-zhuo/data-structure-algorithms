"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        nrow, ncol = len(word1), len(word2)
        res = [range(row, row+ncol+1) for row in range(nrow+1)]
        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                res[i][j] = min(res[i-1][j] + 1, res[i][j-1] + 1, res[i-1][j-1] + (word1[i-1] != word2[j-1]))
        return res[nrow][ncol]