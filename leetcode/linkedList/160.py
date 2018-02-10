# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def getLength(self, head):
        count = 0
        while head != None:
            head = head.next
            count += 1
        return count
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        dif = self.getLength(headA) - self.getLength(headB)
        startA, startB = headA, headB
        if dif > 0: 
            for _ in range(dif):
                startA = startA.next
        else:
            for _ in range(-dif):
                startB = startB.next
        
        while startA != startB:
            startA = startA.next
            startB = startB.next
        
        return startA


a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode(3)
c2 = ListNode(4)
c3 = ListNode(5)
b1 = ListNode(6)
b2 = ListNode(7)
b3 = ListNode(8)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3

b1.next = b2
b2.next = b3
b3.next = c1

s = Solution()
res = s.getIntersectionNode(a1, b1)
print res.val
