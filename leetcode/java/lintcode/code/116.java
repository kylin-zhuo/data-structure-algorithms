public class Solution {
    /*
     * @param A: A list of integers
     * @return: A boolean
     */
    public boolean canJump(int[] A) {
        // write your code here
        int furthest = 0;
        for (int i = 0; i < A.length; i ++) {
            if (i > furthest) return false;
            furthest = Math.max(furthest, i + A[i]);
            if (furthest >= A.length - 1) return true;
        }
        return true;
    }
}