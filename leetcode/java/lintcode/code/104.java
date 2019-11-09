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
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {  
        // write your code here
        Queue<ListNode> pq = new PriorityQueue<ListNode>(11, new Comparator<ListNode>() {
            public int compare(ListNode n1, ListNode n2) {
                return n1.val < n2.val ? -1: (n1.val > n2.val ? 1 : 0);
            }
        });
        for (ListNode n : lists) {
            if (n != null) pq.offer(n);
        }
        ListNode head = new ListNode(0);
        ListNode current = head;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            current.next = node;
            current = current.next;
            if (node.next != null) {
                pq.offer(node.next);
            }
        }
        return head.next;
    }
}
