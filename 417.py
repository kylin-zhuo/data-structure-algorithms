class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        
        def bfs(matrix, visited, queue):
            directions = (0,-1), (-1,0), (0,1), (1,0)
            for q in queue:
                for d in directions:
                    x = q[0] + d[0]
                    y = q[1] + d[1]
                    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[q[0]][q[1]]:
                        continue
                    visited[x][y] = True
                    queue.append((x,y))

        q_atlantic = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
        q_pacific = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        
        v_pacific = [[True] * n] + [([True] + [False] * (n-1)) for _ in range(m-1)]
        v_atlantic = [([False] * (n-1) + [True]) for _ in range(m-1)] + [[True] * n]
        
        bfs(matrix, v_atlantic, q_atlantic)
        bfs(matrix, v_pacific, q_pacific)
        
        return [[i,j] for i in range(m) for j in range(n) if v_atlantic[i][j] and v_pacific[i][j]]