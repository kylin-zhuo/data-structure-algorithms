class ZigzagIterator(object):

    def __init__(self, lists):
        """
        Initialize your data structure here.
        :type lists: List[List[int]]
        """
        self.i = 0
        self.k = len(lists)
        self.lists = lists
        self.lens = map(len, self.lists)
        self.minlen = min(self.lens)
        self.n = sum(self.lens)

        self.row = 0
        self.col = self.minlen

    def next(self):
        """
        :rtype: int
        """
        if self.i < self.minlen * self.k:
            ret = self.lists[self.i % self.k][self.i // self.k]
            self.i += 1
            return ret

        # what if the shortest list runs out of elements??
        while self.col >= self.lens[self.row]:
            self.iterate_row_col()

        self.i += 1
        ret = self.lists[self.row][self.col]
        self.iterate_row_col()
        return ret

    def iterate_row_col(self):
        self.row += 1
        if self.row == self.k:
            self.row = 0
            self.col += 1

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.n


lists = [[1,2,3,4,8,9],[5,6,7],[10,11,12,13],[14,15,16,17,18]]
z = ZigzagIterator(lists)

while z.hasNext():
    print z.next()
