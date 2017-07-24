"""
93 Restore IP address

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, "", 1, s)
        return res

    # Try DFS

    def dfs(self, res, curr, pos, string):
        """
        :param res: the result
        :param curr: current IP address
        :param pos: the position of the dot
        :param string:
        :return:
        """
        if (len(string) == 0) or pos >= 5:
            if (len(string) == 0) and pos == 5:
                res.append(curr[1:])
            return

        for i in range(1, 2 if string[0] == '0' else 4):
            if i > len(string):
                break
            if int(string[:i]) < 256:
                self.dfs(res, curr + '.' + string[:i], pos + 1, string[i:])

s = Solution()
test = "0000"
res = s.restoreIpAddresses(test)
print res