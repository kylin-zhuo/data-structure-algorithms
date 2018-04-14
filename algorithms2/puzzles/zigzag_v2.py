class ZigzagIterator(object):

    def __init__(self, lists):
        self.data = [(len(ls), iter(ls)) for ls in lists if ls]

    def next(self):
        length, it = self.data.pop(0)
        if length > 1:
            self.data.append((length-1, it))
        return next(it)

    def hasNext(self):
        return bool(self.data)


import random
lists = []
for i in range(500):
	tmp = range(1000)
	random.shuffle(tmp)
	lists.append(tmp)
# lists = [[1,2,3,4,8,9],[5,6,7],[10,11,12,13],[14,15,16,17,18]]
z = ZigzagIterator(lists)

while z.hasNext():
    print z.next()