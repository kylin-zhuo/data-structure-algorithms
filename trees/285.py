"""
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.val == root.val:
            return self.rightleftmost(root)
        elif p.val < root.val:
            if not root.left: return None
            if root.left.val == p.val: 
                return root if not p.right else self.rightleftmost(p)
            return root if not self.inorderSuccessor(root.left, p) else self.inorderSuccessor(root.left, p)
        else:
            if not root.right: return None
            if root.right.val == p.val:
                return self.rightleftmost(p)
            return self.inorderSuccessor(root.right, p)
    
    def rightleftmost(self, root):
        if not root: return None
        if not root.right: return None
        curr = root.right
        while curr.left: curr = curr.left
        return curr


# Testing 
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.left.right = TreeNode(7)

p = root.left.left
s = Solution()
print s.inorderSuccessor(root, p)
