public class Solution {
    /*
     * @param n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        // write your code here
        // f(0) = 1
        // f(1) = 1
        // f(2) = f(1)*f(0) + f(0)*f(1)
        // f(3) = f(2)*f(0) + f(1)*f(1) + f(0)*f(2)
        // f(4) = f(3)*f(0) + f(2)*f(1) + f(1)*f(2) + f(0)*f(3)
        // ...
        // f(n) = f(n-1)*f(0) + f(n-2)*f(1) + ... + f(0)*f(n-1)
        
        if (n == 0) return 1;
        int[] dp = new int[n+1];
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = i-1; j >=0; j--) {
                dp[i] += dp[j] * dp[i-j-1];
            }
        }
        return dp[n];
    }
}