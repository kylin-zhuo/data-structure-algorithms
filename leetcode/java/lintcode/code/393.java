public class Solution {
    /*
     * @param K: An integer
     * @param prices: An integer array
     * @return: Maximum profit
     */
    public int maxProfit(int k, int[] prices) {
        // write your code here
        int N = prices.length;
        if (k >= N) return simpleMaxProfit(prices);
        
        int[] local = new int[k + 1];
        int[] global = new int[k + 1];
        int[] prevLocal = new int[k + 1];
        int[] prevGlobal = new int[k + 1];
        
        for (int i = 1; i < N; ++i) {
            prevLocal = local; 
            prevGlobal = global;
            local = new int[k + 1]; 
            global = new int[k + 1];
            int diff = prices[i] - prices[i - 1];
            
            for (int j = 1; j <= k; ++j) {
                local[j] = Math.max(prevGlobal[j - 1], prevLocal[j]) + diff;
                global[j] = Math.max(local[j], prevGlobal[j]);
            }
        }
        return global[k];
    }
    
    int simpleMaxProfit(int[] prices) {
        int N = prices.length;
        if (N <= 1)
                return 0;
        int sum = 0;
        for (int i = 1; i < N; i++) {
                int diff = prices[i] - prices[i - 1];
                if (diff > 0)
                        sum += diff;
        }
        return sum;
    }
    
}