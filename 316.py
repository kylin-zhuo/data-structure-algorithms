"""
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        ctr = Counter(s)
        res = ""
        visited = {}

        for ch in s:

            ctr[ch] -= 1
            if visited.get(ch):
                continue
            while len(res) != 0 and ctr[res[-1]] > 0 and ord(ch) < ord(res[-1]):

                visited[res[-1]] = 0
                res = res[:-1]

            res += ch
            visited[ch] = 1

        return res



s = Solution()
test = "cbacdcbc"
print s.removeDuplicateLetters(test)



        
