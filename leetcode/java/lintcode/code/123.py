from collections import defaultdict, Counter

class Solution(object):

    def exist(self, board, word):
        visited = {}

        if self.is_possible(board, word):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.helper(board, word, i, j, visited):
                        return True
        return False
    
    
    def is_possible(self, board, word):
        ctr = Counter(word)
        return all(sum(map(lambda line: line.count(ch), board)) >= count for ch, count in ctr.items())
    
    
    def helper(self, board, word, i, j, visited, pos = 0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.helper(board, word, i, j + 1, visited, pos + 1) \
                or self.helper(board, word, i, j - 1, visited, pos + 1) \
                or self.helper(board, word, i + 1, j, visited, pos + 1) \
                or self.helper(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res