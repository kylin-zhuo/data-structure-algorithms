"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same_tree(s, t):
            if not s and not t: return True
            if not s and t or s and not t : return False
            return s.val == t.val and same_tree(s.left, t.left) and same_tree(s.right, t.right)
        
        if same_tree(s, t): return True
        if not s and t or s and not t: return False
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # This recursive solution ranks only ~40%


# Try iterative one
class Solution_1(object):

    def isSubtree(self, s, t):
        # Preorder Traversal
        pre_s, pre_t = [], []
        self.preorder(pre_s, s)
        self.preorder(pre_t, t)
        
        # return '$'.join(pre_t) in '$'.join(pre_s)
        return self.verify(pre_s, pre_t)
    
    def verify(self, pre_s, pre_t):
        if not pre_s and not pre_t: return True
        for i in range(len(pre_s)):
            if pre_s[i] == '#': continue 
            if pre_s[i:i+len(pre_t)] == pre_t:
                return True
        return False

    def preorder(self, res, root):
        if not root: 
            res.append('#')
            return
        res.append(str(root.val))
        self.preorder(res, root.left)
        self.preorder(res, root.right) 
        




