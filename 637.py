# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        q = deque([(0, root)])
        dic = dict()
        while q:
            tmp = q.popleft()
            if tmp[1].left:
                q.append((tmp[0] + 1, tmp[1].left))
            if tmp[1].right:
                q.append((tmp[0] + 1, tmp[1].right))
            if tmp[0] not in dic:
                dic[tmp[0]] = [tmp[1].val]
            else:
                dic[tmp[0]].append(tmp[1].val)
        res = []
        for i in range(len(dic)):
            res.append(sum(dic[i]) * 1.0/len(dic[i]))
        return res