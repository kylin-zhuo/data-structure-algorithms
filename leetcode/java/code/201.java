/**
 * Definition of SegmentTreeNode:
 * public class SegmentTreeNode {
 *     public int start, end;
 *     public SegmentTreeNode left, right;
 *     public SegmentTreeNode(int start, int end) {
 *         this.start = start, this.end = end;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param start: start value.
     * @param end: end value.
     * @return: The root of Segment Tree.
     */
    public SegmentTreeNode build(int start, int end) {
        // write your code here
        if (start > end) return null;
        if (start == end) return new SegmentTreeNode(start, end);
        int mid = start + ((end - start) >> 1);
        SegmentTreeNode node = new SegmentTreeNode(start, end);
        SegmentTreeNode left = build(start, mid);
        SegmentTreeNode right = build(mid+1, end);
        node.left = left;
        node.right = right;
        return node;
    }
}