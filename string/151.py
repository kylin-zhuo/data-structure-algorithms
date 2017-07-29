class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([x for x in s.split(' ')[::-1] if x.strip() != ''])


# test = 'the sky is blue'
test = 'afa df    asdfef fds fd fdf efew'
# test = '  '
s = Solution()
print s.reverseWords(test)