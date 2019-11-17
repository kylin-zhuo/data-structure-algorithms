"""

You have a map that marks the locations of treasure islands. 
Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. 
You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. 
Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

Related problems:

    https://leetcode.com/problems/01-matrix

"""
import collections

class Solution(object):

    def shortest_route(self, grid):

        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])

        queue = collections.deque([])

        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    queue.append((i, j))
                    visited[i][j] = True
        
        days = 0

        def neighbors(i, j):
            for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] in ('O', 'X'):
                    visited[x][y] = True
                    yield x, y

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if grid[i][j] == 'X':
                    return days 
                for x, y in neighbors(i, j):
                    queue.append((x,y))
            days += 1
        
        return -1


if __name__ == "__main__":

    s = Solution()

    grid = [['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'D'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']]

    print(s.shortest_route(grid))
