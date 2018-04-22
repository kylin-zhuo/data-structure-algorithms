public class Solution {
    /*
     * @param candidates: A list of integers
     * @param target: An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        int n = candidates.length;
        backtrack(result, new Integer[target], candidates, n - 1, 0, target);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, Integer[] list, int[] candidates, int start, int len, int remain) {
        
        if (remain == 0) {
            Integer[] temp = new Integer[len];
            System.arraycopy(list, 0, temp, 0, len);
            Arrays.sort(temp);
            result.add(Arrays.asList(temp));
        }
        
        if (remain <= 0) return;
        
        for (int i = start; i >= 0; i--) {
            list[len] = candidates[i];
            backtrack(result, list, candidates, i, len + 1, remain - candidates[i]);
        }
    }
}