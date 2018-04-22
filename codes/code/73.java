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
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // write your code here
        if (preorder == null || inorder == null) return null;
        if (preorder.length == 0 || inorder.length == 0) return null;
        return helper(preorder, inorder, 0, preorder.length-1, 0, inorder.length-1);
    }
    
    public TreeNode helper(int[] preorder, int[] inorder, int preStart, int preEnd, int inStart, int inEnd) {
        TreeNode tree = new TreeNode(preorder[preStart]);
        tree.left = null;
        tree.right = null;
        if (preStart == preEnd && inStart == inEnd) return tree;
        int root = 0;
        for (root = inStart; root < inEnd; root ++) {
            if (preorder[preStart] == inorder[root]) break;
        }
        int leftLength = root - inStart;
        int rightLength = inEnd - root;
        if (leftLength > 0) {
            tree.left = helper(preorder, inorder, preStart+1, preStart+leftLength, inStart, root-1);
        }
        if (rightLength > 0) {
            tree.right = helper(preorder, inorder, preStart+1+leftLength, preEnd, root+1, inEnd);
        }
        return tree;
    }
}