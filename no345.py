"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        lis = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s)-1
        while i < j:
            while s[i] not in vowels and i < j: i += 1
            while s[j] not in vowels and j > i: j -= 1
            if s[i] in vowels and s[j] in vowels:
                self.swap(lis, i, j)
            i += 1
            j -= 1
        return ''.join(lis)
    
    def swap(self, lis, i, j):
        tmp = lis[i]
        lis[i] = lis[j]
        lis[j] = tmp            