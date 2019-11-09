def palindrom(s):

	if not s:
		return 0, ''
	n = len(s)
	dp = [[[0, ''] for _ in range(n)] for _ in range(n)]

	for i in range(n):
		dp[i][i] = [1, s[i]]

	for gap in range(1, n):
		for i in range(n-gap):
			j = i+gap
			if s[i] == s[j]:
				dp[i][j][0] = dp[i+1][j-1][0] + 2
				dp[i][j][1] = s[i] + dp[i+1][j-1][1] + s[j]
			else:
				obj = max((dp[i+1][j], dp[i][j-1]), key=lambda x:x[0])
				dp[i][i+gap][0] = obj[0]
				dp[i][i+gap][1] = obj[1]

	return tuple(dp[0][n-1])

s = 'abc121a'
maxlen, string = palindrom(s)
print maxlen
print string