import itertools
from collections import defaultdict

def topologicalSort(edges):
	
	parents = defaultdict(set)
	children = defaultdict(set)

	for v1, v2 in edges:
		parents[v2].add(v1)
		children[v1].add(v2)

	stack = [i for i in set(itertools.chain(*edges)) if not parents[i]]
	res = []

	while stack:
		node = stack.pop()
		res.append(node)
		for ch in children[node]:
			parents[ch].remove(node)
			if not parents[ch]:
				stack.append(ch)
		parents.pop(node)

	return res if not parents else []

edges = [[0,1],[0,3],[1,2],[1,3],[2,5],[2,6],[3,4],[3,7],[4,5],[6,5],[7,4]]
print topologicalSort(edges)