# 311 Sparse Matrix Multiplication

class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        nRowA, nColA, nColB = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in range(nColB)] for _ in range(nRowA)]
        
        table = dict()
        for r, elems in enumerate(B):
            table[r] = {}
            for c, elem in enumerate(elems):
                if elem:
                    table[r][c] = elem
                    
        for i, elemsA in enumerate(A):
            for c, elemA in enumerate(elemsA):
                # enumerate a row:
                if elemA:
                    for j, elemB in table[c].iteritems():
                        res[i][j] += elemA * elemB
        return res