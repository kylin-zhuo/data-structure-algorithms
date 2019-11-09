/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param head: The first node of linked list
     * @param x: An integer
     * @return: A ListNode
     */
    public ListNode partition(ListNode head, int x) {
        
        ListNode smallerHead = new ListNode(0); 
        ListNode biggerHead = new ListNode(0);
        ListNode smaller = smallerHead;
        ListNode bigger = biggerHead;
        
        while (head != null) {
            if (head.val < x) {
                smaller.next = head;
                smaller = smaller.next;
            }
            else {
                bigger.next = head;
                bigger = bigger.next;
            }
            head = head.next;
        }
    
        smaller.next = biggerHead.next;
        bigger.next = null;
        return smallerHead.next;
    }
}