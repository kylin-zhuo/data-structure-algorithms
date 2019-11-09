public class Solution {
    /*
     * @param A: An integer array
     * @param target: An integer
     * @return: An integer
     */
    public int MinAdjustmentCost(List<Integer> A, int target) {

        if (A == null || A.size() == 0) return 0;
        int max = Collections.max(A);
        int[][] costs = new int[A.size()][max+1];
        
        for (int i = 0; i < costs.length; i++) {
            for (int j = 1; j <= max; j++) {
                costs[i][j] = Integer.MAX_VALUE;
                if (i == 0) {
                    costs[i][j] = Math.abs(j - A.get(i));
                } else {
                    for (int k = Math.max(1, j - target); k <= Math.min(j + target, max); k++) {
                        costs[i][j] = Math.min(costs[i][j], Math.abs(j - A.get(i)) + costs[i-1][k]);
                    }
                }
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < costs[0].length; i++) {
            min = Math.min(min, costs[costs.length-1][i]);
        }
        return min;
    }
}