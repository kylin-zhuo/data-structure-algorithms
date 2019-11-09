class Iterator(object):

	def __init__(self, arrayList):
		self.arr = arrayList
		self.p1 = 0
		self.p2 = 0
		self.lens = list(map(lambda x:len(x), arrayList))
		self.N = len(arrayList)
		self.jumpover()

	def hasNext(self):
		if self.p1 >= self.N:
			return False
		if self.p2 < self.lens[self.p1]:
			return True
		return sum(self.lens[self.p1+1:]) > 0

	def next(self):
		ret = self.arr[self.p1][self.p2]
		self.move()
		return ret

	def remove(self, value):
		for i,elem in enumerate(self.arr):
			for j,e in enumerate(elem):
				if e % value == 0:
					elem.pop(j)
					if i == self.p1 and j < self.p2:
						self.p2 -= 1

	def jumpover(self):
		while self.p1 < self.N and not self.arr[self.p1]:
			self.p1 += 1

   	def move(self):
   		if self.p2+1 < self.lens[self.p1]:
   			self.p2 += 1
   		else:
   			self.p2 = 0
   			self.p1 += 1
   			self.jumpover()


# if __name__ == "__main__":

	