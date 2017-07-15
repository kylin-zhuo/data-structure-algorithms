class Solution(object):

    def letterCombinations(self, digits):

		dic = dict({
		1:['*'],
		2:['a','b','c'],
		3:['d','e','f'],
		4:['g','h','i'],
		5:['j','k','l'],
		6:['m','n','o'],
		7:['p','q','r','s'],
		8:['t','u','v'],
		9:['w','x','y','z'],
		0:[' ']
		})
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

test = '234'
s = Solution()
print s.letterCombinations(test)