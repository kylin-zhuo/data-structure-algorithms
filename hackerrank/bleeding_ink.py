import heapq

class Solution(object):   

    def bleedingInk(self, rows, cols, inks):
        grids = [[0] * cols for _ in range(rows)]
        # Start from the ink point with the maximal value
        heap = []
        for val, i, j in inks:
            heapq.heappush(heap, (-val, i, j))
            
        # Recursion for every ink point in the heap
        while heap:
            val, i, j = heapq.heappop(heap)
            # if the current value is greater or equal to the ink, continue
            if grids[i][j] >= -val:
                continue    
            self.dfs(grids, i, j, -val)

        print grids
        return sum(sum(i) for i in grids)


    def dfs(self, grids, i, j, val):
        if 0 <= i < len(grids) and 0 <= j < len(grids[0]) and grids[i][j] < val:
            grids[i][j] = val
            self.dfs(grids, i, j+1, val - 1)
            self.dfs(grids, i, j-1, val - 1)
            self.dfs(grids, i+1, j, val - 1)
            self.dfs(grids, i-1, j, val - 1)

s = Solution()
rows = 8
cols = 10
inks = [(4,1,1), (10,5,5), (2,6,4), (6,3,9)]
a = s.bleedingInk(rows, cols, inks)
