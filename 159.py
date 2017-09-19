class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 2
        if len(set(s)) <= k: return len(s)
        
        dic = {}
        left, right, maxv = 0, 0, 1
        
        while True:
            
            if len(dic) == k and s[right] not in dic:
                maxv = max(maxv, right - left)
                left = min(dic.values()) + 1
                dic.pop(min(dic.items(), key=lambda x: x[1])[0])
                
            dic[s[right]] = right

            if right == len(s) - 1:
                maxv = max(maxv, right - left + 1)
                break
            else:
                right += 1
            
        return maxv
            