class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        num1, num2 = map(int, num1[::-1]), map(int, num2[::-1])
        s1, s2 = len(num1), len(num2)
        table = dict(zip(range(s1 + s2), [0]*(s1 + s2)))
        
        for i in range(s2):
            for j in range(s1):
                prod = num2[i] * num1[j]
                table[i + j] += prod % 10
                table[i + j + 1] += prod / 10
        
        for i in range(len(table) - 1):
            if table[i] >= 10:
                table[i + 1] += table[i] / 10
                table[i] = table[i] % 10
                
        return ''.join([str(table[i]) for i in range(len(table))][::-1]).lstrip('0') or '0'

        