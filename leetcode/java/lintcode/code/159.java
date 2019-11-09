public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        int start = 0;
        int end = nums.length - 1;
        int mid = 0;
        while (nums[start] >= nums[end]) {
            if (end - start == 1) return nums[end];
            mid = start + (end - start) / 2;
            if (nums[mid] < nums[start]) end = mid;
            else if (nums[mid] > nums[end]) start = mid;
        }
        return nums[mid];
    }
}