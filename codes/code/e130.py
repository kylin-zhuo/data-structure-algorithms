class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        m, n = len(board), len(board[0])
        visited = set()
        directions = (1,0), (-1,0), (0,1), (0,-1)
        
        def bfs(i, j):
            queue = [(i, j)]
            flag = True
            for i, j in queue:
                for di, dj in directions:
                    ii = i + di
                    jj = j + dj
                    if board[ii][jj] == 'O' and (ii, jj) not in visited:
                        if not ii or ii == m-1 or not jj or jj == n-1:
                            flag = False
                        else:
                            visited.add((ii, jj))
                            queue.append((ii, jj))
            if flag:
                for i, j in queue:
                    board[i][j] = 'X'
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i,j) not in visited:
                    bfs(i,j)
        
                    