public class Solution {
    /*
     * @param nums: An array of integers
     * @return: An integer
     */
    public int maxProduct(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
        int max = nums[0], min = nums[0];
        int val = max;
        int temp;
        
        for (int i = 1; i < nums.length; i++) {
            temp = max;
            max = Math.max(Math.max(nums[i], temp * nums[i]), min * nums[i]);
            min = Math.min(Math.min(nums[i], temp * nums[i]), min * nums[i]);
            val = Math.max(val, max);
        }
        return val;
    }
}