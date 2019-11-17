"""
You have a map that marks the location of a treasure island. 
Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. 
There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. T
he treasure island is marked as X in a block of the matrix. 
X will not be at the top-left corner.
 Any block with dangerous rocks or reefs will be marked as D. 
 You must not enter dangerous blocks. 
 You cannot leave the map area. 
 Other areas O are safe to sail in. 
 The top-left corner is always safe. 
 Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

"""
import collections 

class Solution(object):
    def find_treasure(self, map):

        if not map or not map[0]:
            return 0

        m, n = len(map), len(map[0])
        
        queue = collections.deque([(0, 0, 0)])
        map[0][0] = '1'

        while queue:
            print(queue)
            print(map)
            day, i, j = queue.popleft()
            for d in ((0,1), (0,-1), (1,0), (-1,0)):
                x, y = i+d[0], j+d[1]
                if 0 <= x < m and 0 <= y < n and map[x][y] in ('O', 'X'):
                    print(i, j, x,y)
                    if map[x][y] == 'X':
                        return day+1
                    queue.append((day+1, x, y))
                    map[x][y] = '1'
        
        return -1


if __name__ == "__main__":
    
    map = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
    s = Solution()
    print(s.find_treasure(map))
