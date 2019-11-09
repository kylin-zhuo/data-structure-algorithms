public class Solution {
    /*
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    public List<Integer> previousPermuation(List<Integer> nums) {
        // write your code here
        if(nums.size() < 2) return nums;
        int i = nums.size() - 1;
        while (i > 0 && nums.get(i) >= nums.get(i-1)) {
            i --;
        }
        if (i <= 0) {
            Collections.reverse(nums);
            return nums;
        }
        int j = i;
        while( j < nums.size() && nums.get(j) < nums.get(i-1)) j++;
        int temp = nums.get(j-1);
        nums.set(j-1, nums.get(i-1));
        nums.set(i-1, temp);
        Collections.sort(nums.subList(i, nums.size()));
        Collections.reverse(nums.subList(i, nums.size()));
        return nums;
    }
}