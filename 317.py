import itertools

class Solution(object):
	def shortestDistance(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		"""
		for example, 
		grid = [[1,0,2,0,1],
				[0,0,0,0,0],
				[0,0,1,0,0]
				]
		"""
		m, n = len(grid), len(grid[0])

		def valid(d):
			return 0 <= d[0] < m and 0 <= d[1] < n and grid[d[0]][d[1]] <= 0

		for i, row in enumerate(grid):
			for j, elem in enumerate(row):
		
				if elem == 1:
					visited = set()
					queue = [((i,j),0)]
					for q in queue:
						depth = q[1]
						c_i, c_j = q[0]
						directions = (c_i+1, c_j), (c_i-1, c_j), (c_i, c_j+1), (c_i, c_j-1)

						for d in directions:
							if valid(d):
								if d not in visited:
									visited.add(d)
									grid[d[0]][d[1]] -= (depth + 1)
									queue.append((d, depth + 1))

		return -max(i for i in itertools.chain(*grid) if i < 0)

grid = [[1,0,2,0,1],
		[0,0,0,0,0],
		[0,0,1,0,0]
		]

print Solution().shortestDistance(grid)