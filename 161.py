"""
161 One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.
"""

class Solution(object):
    
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        if ls == lt:
            return sum(map(lambda x: x[0] != x[1], zip(s, t))) == 1
        elif abs(ls - lt) == 1:
            for i in range(min(ls, lt)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:] or s[i+1:] == t[i:]
            return True
        else:
            return False
            