/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param root: The root of binary tree.
     * @return: An integer
     */
    private int maxv = Integer.MIN_VALUE;
     
    public int maxPathSum(TreeNode root) {
        // write your code here
        helper(root);
        return maxv;
    }
    
    private int helper(TreeNode node) {
        if (node == null) return 0;
        int left = helper(node.left);
        int right = helper(node.right);
        maxv = Math.max(maxv, Math.max(left,0) + Math.max(right,0) + node.val);
        return node.val + Math.max(left, right);
        
    }
}