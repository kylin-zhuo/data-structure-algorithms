public class Solution {
    /*
     * @param num: A list of integers
     * @return: An integer
     */
    public int longestConsecutive(int[] num) {
        // write your code here
        Set<Integer> set = new HashSet<Integer>();
        for (int n:num) set.add(n);
        int maxv = 0, count;
        for (int n:num) {
            if (!set.contains(n-1)) {
                count = 0;
                while (set.contains(n)) {
                    count ++;
                    n += 1;
                }
                maxv = Math.max(maxv, count);
            }
        }
        return maxv;
    }
}