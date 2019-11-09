public class Solution {
    /*
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumberII(int[] A) {
        // write your code here
        int[] B = new int[32];
        for (int j = 0; j < A.length; j ++) {
            for (int i = 0; i < 32; i ++) {
                if ( ((1<<i) & A[j]) == 1<<i) B[i] = (B[i] + 1) % 3;
            }
        }
        int res = 0;
        for (int i = 0; i < 32; i ++) res = res * 2 + B[31-i];
        return res;
    }
}