class Trie(object):
    
    def __init__(self, nums):
        self.nums = nums
        self.root = [{}, 0]
        for n in nums:
            self.insert(n)
    
    # the format of node: [dict{'1': another node, '0': another node}, level]

    def insert(self, n):
        binary = '{:032b}'.format(n)
        node = self.root
        for bit in binary:
            bit = int(bit)
            if bit not in node[0]:
                node[0][bit] = [{}, node[1] + 1]
            node = node[0][bit]
                

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # build a 32-level Trie
        # go down through the Trie level by level from the root
        tr = Trie(nums)
        root = tr.root

        while len(root[0].keys()) == 1:
            root = root[0][root[0].keys()[0]]

        if not root[0].keys():
            return 0

        def helper_xor(node1, node2):
            if not node1[0] and not node2[0]:
                return 1 << (32 - node1[1])

            len1 = len(node1[0].keys())
            len2 = len(node2[0].keys())

            if len1 == len2 == 1:
                print (1 << (32 - node1[1])) * node1[0].keys()[0], node1[1]
                return helper_xor(node1[0].values()[0], node2[0].values()[0]) + (1 << (32 - node1[1])) * node1[0].keys()[0]

            elif len1 == 1 and len2 == 2:
                key1 = node1[0].keys()[0]
                print 1 << (32 - node1[1]), node1[1]
                return helper_xor(node1[0][key1], node2[0][1-key1]) + (1 << (32 - node1[1])) * 1

            elif len1 == 2 and len2 == 1:
                key2 = node2[0].keys()[0]
                print 1 << (32 - node2[1]), node2[1]
                return helper_xor(node1[0][1-key2], node2[0][key2]) + (1 << (32 - node2[1])) * 1

            elif len1 == len2 == 2:
                keys1 = node1[0].keys()
                res1 = helper_xor(node1[0][keys1[0]], node2[0][1-keys1[0]])
                res2 = helper_xor(node1[0][keys1[1]], node2[0][1-keys1[1]])

                return max (res1, res2) + (1 << (32 - node1[1]))

        return helper_xor(root[0][0], root[0][1])


input = [3, 10, 5, 25, 2, 8]
s = Solution()

print s.findMaximumXOR(input)