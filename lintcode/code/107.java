public class Solution {
    /*
     * @param s: A string
     * @param dict: A dictionary of words dict
     * @return: A boolean
     */
    public boolean wordBreak(String s, Set<String> dict) {
        // write your code here
        int n = s.length();
        boolean[] dp = new boolean[n+1];
        dp[n] = true;
        
        for (int i = n-1; i >= 0; i --) {
            for (int j = n; j >= i; j --) {
                if (dict.contains(s.substring(i, j)) && dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }

    // 上面那个方法会超时，该方法较优。
    public boolean wordBreak2(String s, Set<String> dict) {
        // write your code here
        if (s == null || s.length() == 0) return true;
        int n = s.length();
        boolean[] res = new boolean[n+1];
        res[0] = true;
        
        for (int i = 0; i < n; i ++) {
            if (!res[i]) continue;
            else {
                for(String str:dict) {
                    int end = i + str.length();
                    if (end > n) continue;
                    if (s.substring(i,end).equals(str)) res[end] = true;
                }
            }
        }
        return res[n];
    }
}