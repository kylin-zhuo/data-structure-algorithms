"""
Given n ropes of different lengths, we need to connect these ropes into one rope. 
We can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. 
The length of this connected rope is also equal to the sum of their lengths. 
This process is repeated until n ropes are connected into a single rope. 
Find the min possible cost required to connect all ropes.

Example 1:

Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58

Example 2:

Input: ropes = [20, 4, 8, 2]
Output: 54

Example 3:

Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224

Example 4:

Input: ropes = [2, 2, 3, 3]
Output: 20

"""

from heapq import heappush, heappop, heapify

import unittest

class Solution():

    def min_cost(self, ropes):

        heapify(ropes)
        res = 0

        while len(ropes) >= 2:
            cost = heappop(ropes) + heappop(ropes)
            res += cost
            heappush(ropes, cost)

        return res


class Test(unittest.TestCase):

    s = Solution()

    def test1(self):
        ropes = [8, 4, 6, 12]
        self.assertEqual(self.s.min_cost(ropes), 58)

    def test2(self):
        ropes = [20, 4, 8, 2]
        self.assertEqual(self.s.min_cost(ropes), 54)

    def test3(self):
        ropes = [1, 2, 5, 10, 35, 89]
        self.assertEqual(self.s.min_cost(ropes), 224)

    def test4(self):
        ropes = [2, 2, 3, 3]
        self.assertEqual(self.s.min_cost(ropes), 20)

    def test5(self):
        ropes = [1000]
        self.assertEqual(self.s.min_cost(ropes), 0)

    def test6(self):
        ropes = []
        self.assertEqual(self.s.min_cost(ropes), 0)

    def test7(self):
        ropes = [1000, 1]
        self.assertEqual(self.s.min_cost(ropes), 1001)


if __name__ == "__main__":
    unittest.main()