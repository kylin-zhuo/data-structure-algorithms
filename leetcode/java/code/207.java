public class Solution {
    /* you may need to use some attributes here */

    /*
    * @param A: An integer array
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
    
    private SegTreeNode root;
    private int[] nums;
    
    public Solution(int[] A) {
        // do intialization if necessary
        if (A == null || A.length == 0) {
            root = null;
        } else {
            root = construct(0, A.length-1, A);
            nums = A;
        }
    }

    /*
     * @param start: An integer
     * @param end: An integer
     * @return: The sum from start to end
     */
    public long query(int start, int end) {
        return queryHelper(root, start, end);
    }
    
    long queryHelper(SegTreeNode root, int start, int end) {
        if (root == null) return Integer.MAX_VALUE;  
        if (start <= root.start && end >= root.end) return root.sum;  
        int mid = (root.start + root.end) / 2;  
        if (mid < start) return queryHelper(root.right, start, end);  
        else if(end < mid+1) return queryHelper(root.left, start, end);  
        else return queryHelper(root.left, start, mid) + queryHelper(root.right, mid+1, end);  
    }

    /*
     * @param index: An integer
     * @param value: An integer
     * @return: nothing
     */
    public void modify(int index, int value) {
        // write your code here
        modifyHelper(root, index, value);
    }
    
    void modifyHelper(SegTreeNode root, int index, int value) {
        if (index < root.start || index > root.end) return;
        nums[index] = value;
        if (index == root.start && index == root.end) {
            root.sum = value;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (index <= mid) modifyHelper(root.left, index, value);
        else modifyHelper(root.right, index, value);
        root.sum = root.left.sum + root.right.sum;
    }
}