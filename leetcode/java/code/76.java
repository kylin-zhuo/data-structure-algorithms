public class Solution {
    /*
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i ++) {
            int pos = search(list, 0, list.size(), nums[i]);
            if (pos >= list.size()) list.add(nums[i]);
            else list.set(pos, nums[i]);
        }
        return list.size();
    }
    
    public int search(List<Integer> nums, int left, int right, int target) {
        if (left == right) return left;
        int mid = left + ((right - left) >> 1);
        if (nums.get(mid) < target) return search(nums, mid+1, right, target);
        else return search(nums, left, mid, target);
    }
}