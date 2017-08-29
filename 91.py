"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) <= 1:
            return 0 if not s else 1 if int(s) else 0
        
        res = [1, 1] + [0] * (len(s) - 1)
        s = '0' + s
        i = 1
        
        while i < len(s):
            if s[i] == '0' or (i < len(s) - 1 and s[i+1] == '0' and int(s[i]) > 2):
                return 0
            elif i < len(s) - 1 and s[i+1] == '0':
                res[i] = res[i-1]
                res[i+1] = res[i-1]
                i += 1
            elif int(s[i-1:i+1]) > 26 or s[i-1] == '0':
                res[i] = res[i-1]
            else:
                res[i] = res[i-1] + res[i-2]
            i += 1

        return res[-1]