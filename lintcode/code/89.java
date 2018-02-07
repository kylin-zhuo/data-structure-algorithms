public class Solution {
    /*
     * @param A: An integer array
     * @param k: A positive integer (k <= length(A))
     * @param target: An integer
     * @return: An integer
     */
    public int kSum(int[] A, int k, int target) {
        // write your code here
        int[][] dp = new int[k+1][target+1];
        dp[0][0] = 1;
        
        for(int x = 0; x < A.length; x++) {
            for (int i = k; i >= 1; i--) {
                for (int j = target; j >= A[x]; j--) {
                    dp[i][j] += dp[i-1][j-A[x]];
                }
            }
        }
        return dp[k][target];
    }
}