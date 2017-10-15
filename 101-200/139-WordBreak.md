### Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
`s = "leetcode",
dict = ["leet", "code"].
`

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

----------
动态规划求解。建立一个状态数组dp，其长度为len(s)+1。dp[i]表示从第i个位置到词尾是否有可行的组合。则dp[len(s)]应该初始化为True。

动态转移方程为：

对于第i个位置，考虑从dp[i+1] ~ dp[len(s)]当中的值（假设称其为dp[j]），当其为True（即表示从第j个位置到词尾存在可行组合）并且s[i:j]是一个存在的词，则说明dp[i]可以通过组合接到词尾。

`any(dp[j] and s[i:j] in words for j=i+1 to len(s))`

```
def wordBreak(s, wordList):

	words = set(wordList)
	dp = [False] * len(s) + [True]

	for i in range(len(s))[::-1]:
		dp[i] = any(dp[j] and s[i:j] in words for j in range(i+1, len(s)+1))

	return dp[0]

s = 'leetcode'
wordList = ['leet', 'code']

print wordBreak(s, wordList)
```
