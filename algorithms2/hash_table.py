class HashTable(object):

	def __init__(self, size):
		self.size = size
		self.data = [[] for _ in range(size)]

	def getHashCode(self, key):
		return hash(key)

	def convertToIndex(self, hashCode):
		return hashCode % self.size

	def put(self, key, value):
		hashCode = self.getHashCode(key)
		index = self.convertToIndex(hashCode)
		linkedlist = self.data[index]
		linkedlist.append((key, value))

	def get(self, key, default=None):
		index = self.convertToIndex(self.getHashCode(key))
		linkedlist = self.data[index]
		for i, (k, v) in enumerate(linkedlist):
			if k == key:
				return v
		if default is not None:
			return default 
		else:
			raise Exception

	def printTable(self):
		print self.data

	def numCollision(self):
		return sum(filter(lambda x: x > 0, map(lambda x: len(x)-1, self.data)))


ht = HashTable(19)

states = [('California', 39.25), 
('Texas', 27.86), 
('Florida', 20.61), 
('New York', 19.75),
('Illinois', 12.80),
('Pennsylvania', 12.78),
('Ohio', 11.65),
('Georgia', 10.31),
('North Carolina', 10.15),
('Michigan', 9.93)
]
for name, pop in states:
	ht.put(name, pop)

ht.printTable()
print ht.get('Texas')
print ht.get('Michigan')
print ht.get('XXX', 0)
print ht.numCollision()

# raise exception
# print ht.get('YYY')

