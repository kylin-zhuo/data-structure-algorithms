from collections import defaultdict, deque

def wordLadder(beginWord, endWord, wordList):

	dic = defaultdict(set)
	for word in wordList:
		for i in range(len(word)):
			key = word[:i] + '*' + word[i+1:]
			dic[key].add(word)

	queue = deque([(1, beginWord)])
	visited = set()

	parents = {}
	ret = None

	while queue:
		d, word = queue.popleft()
		if word == endWord:
			ret = d
			break
		if word not in visited:
			visited.add(word)
			for i in range(len(word)):
				tmp = word[:i] + '*' + word[i+1:]
				neighbors = dic.get(tmp, [])
				for n in neighbors:
					if n not in visited:
						parents[n] = word
						queue.append((d+1, n))

	if not ret:
		return 0, ""
	else:
		w, path = endWord, [endWord]
		while w in parents and parents[w] != beginWord:
			w = parents[w]
			path.append(w)
		path.append(beginWord)
		return ret, '->'.join(path[::-1])


beginWord = "lot"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

steps, order = wordLadder(beginWord, endWord, wordList)
print steps, order