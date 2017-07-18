"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.maxv = 0
        self.helper(root, 1)
        
        return self.maxv
    
    def helper(self, root, curr):
        if curr > self.maxv: self.maxv = curr
        if not root: return
        if root.left:
            if root.left.val == root.val + 1:
                self.helper(root.left, curr + 1)
            else:
                self.helper(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.helper(root.right, curr + 1)
            else:
                self.helper(root.right, 1)
            