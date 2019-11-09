class Solution(object):
    
    def peek(self, stack, s):
        if len(stack) == 0:
            return ''
        else:
            return s[stack[-1]]
            
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, l = [], len(s)
        for i in range(l):
            if s[i] == ')':
                if self.peek(stack, s) == '(':
                    stack.pop()
                else:
                    stack.append(i)
                        
            elif s[i] == '(':
                stack.append(i)
            else:
                print 'error in input'
        # print stack
        # print len(s)
        max_count = None
        if len(stack) == 0:
            max_count = l
        else:
            a,b = l,0
            while len(stack) > 0:
                b = stack[-1]
                stack.pop()
                max_count = max(max_count, a-b-1)
                a = b
            max_count = max(max_count, a)
        return max_count

s = Solution()
test = '()()))()))()()()()()()'
print s.longestValidParentheses(test)