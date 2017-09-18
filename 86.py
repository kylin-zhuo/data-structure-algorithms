# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        temp = ListNode(float('-inf'))
        temp.next = head
        left, right = temp, temp
        
        while right.next and right.val < x:
            right = right.next
        
        while True:
            while right.next and right.next.val >= x:
                right = right.next
            if not right.next:
                break
            while left.next and left.next.val < x:
                left = left.next
            
            tmp = left.next
            left.next = right.next
            right.next = right.next.next
            left.next.next = tmp
        
        return temp.next