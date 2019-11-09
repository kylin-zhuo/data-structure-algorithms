from collections import defaultdict

def manager_score(n, data):
	# employee id from 0 to n-1
	scores = [0] * n
	subordinates = defaultdict(set)
	roots = []

	for i, d in enumerate(data):
		scores[i] = d[0]
		if d[1] == -1:
			roots.append(i)
		else:
			subordinates[d[1]].add(i)

	def dfs(node):
		# if the employee has no subordinates, return
		if node not in subordinates:
			return
		subs = subordinates[node]
		for s in subs:
			scores[s] = min(scores[s], scores[node])
			dfs(s)

	for r in roots:
		dfs(r)
		
	return sum(scores)


