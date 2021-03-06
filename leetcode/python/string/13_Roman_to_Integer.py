class Solution(object):
	
    def romanToInt(self, s):
        if not s: return 0
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        # MMMCDXXIX
        # = 1000+1000+1000-100+500+10+10-1+10
        res = 0
        for i in range(len(s)-1):
            res += dic[s[i]] * (-1 if dic[s[i]] < dic[s[i+1]] else 1)
        return res + dic[s[-1]]
