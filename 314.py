# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # for a root that is at layer i, 
        # its left child is at layer i-1 and right child at layer i+1.
        if not root: return []
        table = {}
        q = deque([(0, root)])
        while q:
            node = q.popleft()
            if node[1].left:
                q.append((node[0] - 1, node[1].left))
            if node[1].right:
                q.append((node[0] + 1, node[1].right))
            if node[0] not in table:
                table[node[0]] = [node[1].val]
            else:
                table[node[0]].append(node[1].val)

        return [table[layer] for layer in sorted(table)]
        
        