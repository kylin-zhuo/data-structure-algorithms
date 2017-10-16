def wordBreak(s, wordList):

	words = set(wordList)
	dp = [False] * len(s) + [True]

	for i in range(len(s))[::-1]:
		dp[i] = any(dp[j] and s[i:j] in words for j in range(i+1, len(s)+1))

	return dp[0]

s = 'leetcode'
wordList = ['leet', 'code']

print wordBreak(s, wordList)