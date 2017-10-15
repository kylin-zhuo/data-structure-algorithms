import collections

def wordSquares(words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words or not words[0]:
        	return []
        m, n = len(words), len(words[0])
        dic = collections.defaultdict(set)

        for word in words:
        	for i in range(n):
        		dic[word[:i]].add(word)
        
        cur, res = [], []	
        
        def backtrack(word, pos):
            cur.append(word)
            if pos == n:
                res.append(cur[:])
            else:
                prefix = ''.join(cur[x][pos] for x in range(pos))
                for w in dic[prefix]:
                    backtrack(w, pos + 1)
            cur.pop()
            
        for w in words:
            backtrack(w, 1)
            
        return res

words = ['ball', 'area', 'lead', 'lady', 'wall']
print wordSquares(words)