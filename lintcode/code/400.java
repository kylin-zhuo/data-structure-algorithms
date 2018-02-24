public class Solution {
    /*
     * @param nums: an array of integers
     * @return: the maximun difference
     */
    public int maximumGap(int[] nums) {
        // write your code here
        if (nums.length < 2) return 0;
        int n = nums.length;
        long min = Long.MAX_VALUE;
        long max = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, nums[i]);
            max = Math.max(max, nums[i]);
        }
        long bucketCapacity = (max - min) / n + 1;
        int nBuckets = (int) ((max - min) / bucketCapacity) + 1;
        long[] mins = new long[nBuckets];
        long[] maxs = new long[nBuckets];
        for(int i = 0; i < nBuckets; i++) {
            mins[i] = Long.MAX_VALUE;
            maxs[i] = Long.MIN_VALUE;
        }
        int index;
        for (int num:nums) {
            index = (int) ((num - min) / bucketCapacity);
            mins[index] = Math.min(mins[index], num);
            maxs[index] = Math.max(maxs[index], num);
        }
        long result = Long.MIN_VALUE;
        int pre = 0;
        for (int i = 1; i < nBuckets; i++) {
            if (mins[i] == Long.MAX_VALUE || maxs[i] == Long.MIN_VALUE) {
                continue;
            }
            result = Math.max(result, mins[i] - maxs[pre]);
            pre = i;
        }
        return (int) result;
    }
}