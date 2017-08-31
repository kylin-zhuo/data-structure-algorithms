"""
282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

"""

class Solution(object):
    
    def addOperators(self, num, target):
        # Backtracking 
        if not num:
            return []
        res = []
        self.helper(res, num, 0, "", target, 0)
        return res
        
        
    def helper(self, res, num, pos, curr_string, rest, last):
        
        if pos == len(num):
            if rest == 0:
                res.append(curr_string)
            return 
        
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            curr = int(num[pos:i+1])
            if pos == 0:
                self.helper(res, num, i + 1, curr_string + str(curr), rest - curr, curr)
            else:
                self.helper(res, num, i + 1, curr_string + "+" + str(curr), rest - curr, curr)
                self.helper(res, num, i + 1, curr_string + "-" + str(curr), rest + curr, -curr)
                self.helper(res, num, i + 1, curr_string + "*" + str(curr), rest + last - last * curr, last * curr)
            
            