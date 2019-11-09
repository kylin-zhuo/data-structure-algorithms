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
     * @param root: A Tree
     * @return: Inorder in ArrayList which contains node values.
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        // write your code here
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> result = new ArrayList<Integer>();
        
        if (root == null) return result;
        pushAllLeft(stack, root);
        
        while (!stack.empty()) {
            TreeNode current = stack.pop();
            result.add(current.val);
            if (current.right != null) pushAllLeft(stack, current.right);
        }
        return result;
    }
    
    public void pushAllLeft(Stack<TreeNode> stack, TreeNode node) {
        stack.push(node);
        TreeNode current = node;
        while (current.left != null) {
            current = current.left;
            stack.push(current);
        }
    }
}