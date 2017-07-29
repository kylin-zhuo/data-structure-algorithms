"""
366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def assign_height(root, dic):
            if not root: return 0
            l = assign_height(root.left, dic)
            r = assign_height(root.right, dic)
            height = max(l, r) + 1
            if height not in dic: dic[height] = []
            dic[height].append(root.val)
            return height
        
        dic = {}
        assign_height(root, dic)
        return [dic[i] for i in range(1, len(dic) + 1)]