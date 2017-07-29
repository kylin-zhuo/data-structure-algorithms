# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        
        temp = ListNode(0)
        curr, pre, next = head, temp, None
        
        while curr:
            next = curr.next
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            curr.next = pre.next
            pre.next = curr
            pre = temp
            curr = next
            
        return temp.next