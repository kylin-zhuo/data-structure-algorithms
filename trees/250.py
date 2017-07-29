"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        def helper(root):
            if not root: return True
            l, r = helper(root.left), helper(root.right)
            if not l or not r or root.left and root.val != root.left.val or root.right and root.val != root.right.val:
                return False
            self.count += 1
            return True
        helper(root)
        return self.count