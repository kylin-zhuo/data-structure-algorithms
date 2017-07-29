/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> rst = new ArrayList<List<Integer>>();
        List<Integer> solution = new ArrayList<Integer>();

        findSum(rst, solution, root, sum);
        return rst;
    }
    
    // Manipulation on the result and solution
    private void findSum(List<List<Integer>> result, List<Integer> solution, TreeNode current, int sum){
        if (current == null) {
            return;
        }
        
        // substract current node's value out from the goal
        sum -= current.val;

        // if the current node is a leaf
        if (current.left == null && current.right == null) {
            if (sum == 0){
                solution.add(current.val);
                result.add(new ArrayList<Integer>(solution));
                solution.remove(solution.size()-1);
            }
            return;
        }

        solution.add(current.val);
        findSum(result, solution, current.left, sum);
        findSum(result, solution, current.right, sum);
        solution.remove(solution.size()-1);
    }
}