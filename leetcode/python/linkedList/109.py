"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.helper(head)

    def helper(self, head):

    	if not head: return None
    	if not head.next: return TreeNode(head.val)

    	slow, fast = head, head.next.next
    	while fast and fast.next:
    		fast = fast.next.next
    		slow = slow.next

    	node2 = slow.next.next
    	root = TreeNode(slow.next.val)
    	slow.next = None
    	node1 = head

    	root.left = self.helper(node1)
    	root.right = self.helper(node2)
    	return root


s = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)

res = s.sortedListToBST(root)
print res.left.val








        
