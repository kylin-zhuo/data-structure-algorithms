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
     * @param root: The root of the binary search tree.
     * @param value: Remove the node with given value.
     * @return: The root of the binary search tree after removal.
     */
    public TreeNode removeNode(TreeNode root, int value) {
        // write your code here
        // 先通过递归找到要删除节点的位置，然后找到要删除节点的右子树中最小的点，将它赋值给要删除的节点，然后删除节点。
        
        if (root == null) return root;
        if (root.val > value) root.left = removeNode(root.left, value);
        else if (root.val < value) root.right = removeNode(root.right, value);
        else if (root.left != null && root.right != null) {
            root.val = findMin(root.right);
            removeNode(root.right, root.val);
        }
        else root = root.left != null ? root.left:root.right;
        return root;
    }
    
    private int findMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node.val;
    }
}