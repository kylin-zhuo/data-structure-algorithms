def longestValidParenthesis(string):

	stack = [-1]
	maxv = 0
	for i,c in enumerate(string):
		if c == '(':
			stack.append(i)
		else:
			stack.pop()
			if stack:
				maxv = max(maxv, i-stack[-1])
			else:
				stack.append(i)
	return maxv

test = ['((()()', '()(()))))', '))())(((())()))']

for t in test:
	print longestValidParenthesis(t)