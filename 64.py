class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: 
            return 0
        import copy
        res = copy.deepcopy(grid)
        nrow, ncol = len(grid), len(grid[0])
        for j in range(1, ncol):
            res[0][j] = res[0][j-1] + grid[0][j]
        for i in range(1, nrow):
            res[i][0] = res[i-1][0] + grid[i][0]
            
        for i in range(1, nrow):
            for j in range(1, ncol):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        
        return res[nrow-1][ncol-1]