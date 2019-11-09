class Main:

	def __init__(self):
		self.V = None
		self.count = 0

	def countCycles(self, graph, n):
		self.V = len(graph)
		marked = [False] * self.V

		for i in range(self.V-(n-1)):
			self.dfs(graph, marked, n-1, i, i)
			marked[i] = True

		return self.count // 2

	def dfs(self, graph, marked, n, vert, start):
		marked[vert] = True
		if not n:
			marked[vert] = False
			if graph[vert][start] == 1:
				self.count += 1
			return

		for i in range(self.V):
			if not marked[i] and graph[vert][i] == 1:
				self.dfs(graph, marked, n-1, i, start)

		marked[vert] = False

main = Main()
graph = [[0,1,0,1,0],
		 [1,0,1,0,1],
		 [0,1,0,1,0],
		 [1,0,1,0,1],
		 [0,1,0,1,0]]
n = 4
print main.countCycles(graph, n)