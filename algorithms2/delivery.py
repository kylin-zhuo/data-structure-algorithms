def delivery(m, n, D):

	D = set(D)

	dp = [[0 for _ in range(m)] for _ in range(n)]
	path = [(m-1, n-1)]

	for i in range(m):
		for j in range(n):
			top = 0 if not i else dp[i-1][j]
			left = 0 if not j else dp[i][j-1]
			dp[i][j] = int((i,j) in D) + max(top,left)

	pi, pj = m-1, n-1
	while pi or pj:
		if not pi:
			path.append((pi, pj-1))
			pj -= 1
		elif not pj or dp[pi-1][pj] > dp[pi][pj-1]: 
			path.append((pi-1, pj))
			pi -= 1 
		else:
			path.append((pi, pj-1))
			pj -= 1

	return dp[m-1][n-1], '->'.join(map(str, path[::-1]))

D = [(1,2), (2,1), (3,1), (3,2)]

maxv, path = delivery(4, 4, D)
print maxv
print path
