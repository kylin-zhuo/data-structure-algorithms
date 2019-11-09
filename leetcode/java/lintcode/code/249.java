public class Solution {
    /*
     * @param A: an integer array
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    
    int count = 0; // the class paramter
    
    private class TreeNode {
        TreeNode left = null;
        TreeNode right = null;
        int val = 0; // the value of node
        int numVal = 1; // the number of values
        int nLeft = 0; // the number of nodes in left subtree
    }
    
    void insert(TreeNode root, int val) {
        if (root.val == val) {
            root.numVal += 1;
            count += root.nLeft;
            return;
        } else if (val < root.val) {
            root.nLeft ++;
            if (root.left == null) {
                TreeNode node = new TreeNode();
                node.val = val;
                root.left = node;
                return;
            } else { insert(root.left, val); }
        } else {
            count += (root.nLeft + root.numVal); // save the stage result
            if (root.right == null) {
                TreeNode node = new TreeNode();
                node.val = val;
                root.right = node;
                return;
            } else { insert(root.right, val); }
        }
        
    }
    
    public List<Integer> countOfSmallerNumberII(int[] A) {
        // write your code here
        List<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0) return res;
        TreeNode root = new TreeNode();
        root.val = A[0];
        res.add(count);
        
        for(int i = 1; i < A.length; i++) {
            int current = A[i];
            count = 0; // start from zero
            insert(root, current);
            res.add(count);
        }
        return res;
    }
}