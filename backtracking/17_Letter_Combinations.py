class Solution(object):

    def letterCombinations(self, digits):
		dic = (' ','*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz')
		res = []
		if digits: res.append("")
		for i in range(len(digits)):
			ds = dic[int(digits[i])]
			while(len(res[0]) == i):
				t = res[0]
				res = res[1:]
				for s in ds:
					res.append(t+s)
		return res

    def letterCombinations(self, digits):
        if not digits: return []
        dic = (' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        res = []
        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            for c in dic[int(digits[i])]:
                dfs(i+1, cur+c)
        dfs(0, "")
        return res
