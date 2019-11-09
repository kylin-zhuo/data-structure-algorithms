# The knight's Tour Problem
# Print the visit order of a knight covering all the cells

def knightTour(nrow, ncol):

	res = [[-1 for _ in range(ncol)] for _ in range(nrow)]
	directions = (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)

	def backtrack(i, j, step_no):

		if step_no == nrow * ncol:
			return True

		for di, dj in directions:
			if 0 <= i+di < nrow and 0 <= j+dj < ncol and res[i+di][j+dj] == -1:
				res[i+di][j+dj] = step_no
				if backtrack(i+di, j+dj, step_no+1):
					return True
				else:
					res[i+di][j+dj] = -1
		return False

	res[0][0] = 0
	if not backtrack(0,0,1):
		print("Solution does not exist.")
	else:
		print(res)

knightTour(8,8)
