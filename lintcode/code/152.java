public class Solution {
    /*
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    public List<List<Integer>> combine(int n, int k) {
        // write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        backtrack(result, new ArrayList<Integer>(), 0, 0, n, k);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> current, int num, int maxv, int n, int k) {
        if (num == k) {
            result.add(new ArrayList<Integer>(current));
        }
        if (maxv > n) return;
        for (int i = maxv + 1; i <= n; i ++) {
            List<Integer> temp = new ArrayList<Integer>(current);
            temp.add(i);
            backtrack(result, temp, num + 1, i, n, k);
        }
    }
}