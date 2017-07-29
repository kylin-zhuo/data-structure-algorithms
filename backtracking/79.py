"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

from collections import defaultdict

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
        character_counts = defaultdict(int)
        for ch in word:
            character_counts[ch] += 1
        return all(sum(map(lambda line: line.count(ch), board)) >= count for ch, count in character_counts.items())
    
    
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