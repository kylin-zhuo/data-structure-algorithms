public class Solution {
    /*
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // write your code here
        Arrays.sort(nums);
        backtrack(new ArrayList<Integer>(), nums, 0);
        return res;
    }
    
    private void backtrack(List<Integer> cur, int[] nums, int pos) {
        res.add(new ArrayList<Integer>(cur));
        for (int i = pos; i < nums.length; i++) {
            if (i > pos && nums[i] == nums[i-1]) continue;
            List<Integer> list = new ArrayList<Integer>(cur);
            list.add(nums[i]);
            backtrack(list, nums, i+1);
        }
    }
}