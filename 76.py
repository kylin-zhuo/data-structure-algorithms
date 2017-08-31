from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Two Pointers and Hash Table
        ctr = Counter(t)
        i = 0
        res = (float('inf'), (0, 0)) 
        while s[i] not in ctr:
            i += 1
        ctr[s[i]] -= 1
        j = i
        
        while j < len(s) - 1:
            while max(ctr.values()) > 0 and j < len(s) - 1:
                j += 1
                if s[j] in ctr:
                    ctr[s[j]] -= 1
            res = min(res, (j - i + 1, (i, j)))
            print res
            
            ctr[s[i]] += 1
            tmp = s[i]
                
            while i < j:
                i += 1
                if s[i] in ctr:
                    break
                    
            if max(ctr.values()) <= 0:
                res = min(res, (j - i + 1, (i, j)))
                print res
        
        
        return s[res[1][0]:res[1][1]+1]


s = Solution()
S = "ADOBECODEBANC"
T = "ABC"

print s.minWindow(S, T)