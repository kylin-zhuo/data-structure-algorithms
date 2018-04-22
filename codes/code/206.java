/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */


public class Solution {
    /*
     * @param A: An integer list
     * @param queries: An query list
     * @return: The result list
     */
     
    private class SegTreeNode {
        int start;
        int end;
        long sum;
        SegTreeNode left = null;
        SegTreeNode right = null;
        
        SegTreeNode (int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    
    private SegTreeNode construct(int start, int end, int[] A) {
        if (start == end) {
            SegTreeNode leaf = new SegTreeNode(start, end);
            leaf.sum= (long) A[start];
            return leaf;
        }
        int mid = (start + end) / 2;
        SegTreeNode left = construct(start, mid, A);
        SegTreeNode right = construct(mid+1, end, A);
        SegTreeNode node = new SegTreeNode(start, end);
        node.sum = left.sum + right.sum;
        node.left = left;
        node.right = right;
        return node;
    }
    
    private long query(SegTreeNode root, int start, int end) {
        if (root == null) return Integer.MAX_VALUE;  
        if (start <= root.start && end >= root.end) return root.sum;  
        int mid = (root.start + root.end) / 2;  
        if (mid < start) return query(root.right, start, end);  
        else if(end < mid+1) return query(root.left, start, end);  
        else return query(root.left, start, mid) + query(root.right, mid+1, end);  
    }
    
    public List<Long> intervalSum(int[] A, List<Interval> queries) {
        // write your code here
        int n = A.length;
        SegTreeNode root = construct(0, n-1, A);
        List<Long> res = new ArrayList<Long>();
        for (Interval it:queries) {
            res.add(query(root, it.start, it.end));
        }
        return res;
    }
}