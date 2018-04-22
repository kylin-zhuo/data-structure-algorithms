public class Solution {
    /*
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        
        if (nums == null || nums.length == 0) return 0;
        int left = 0;
        int right = nums.length - 1;
        int i = 0;
        
        while (left < right) {
            if (nums[left] >= k) {
                swap(nums, left, right);
                right -= 1;
            } else {
                left += 1;
            }
        }
        return nums[left] >= k ? left:left+1;
    }
    
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}