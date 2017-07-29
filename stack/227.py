# 227. Basic Calculator II

# idea: use stack 

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
        	return 0

        stack, op = [], '+'
        num = 0

        for i in range(len(s)):
        	if s[i].isdigit():
        		num = num * 10 + ord(s[i]) - ord('0')
        		pass
        	if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
        		if op == '+':
        			stack.append(num)
        		elif op == '-':
        			stack.append(-num)
        		elif op == '*':
        			stack.append(stack.pop() * num)
        		else: # the case of '/'
        			tmp = stack.pop()
        			if tmp//num < 0 and tmp%num != 0:
        				stack.append(tmp//num + 1)
        			else:
        				stack.append(tmp//num)
        		num = 0
        		op = s[i]

        return sum(stack)

test = '3-4*2+3+5/2*3*3*2'

s = Solution();
print s.calculate(test)