public class Solution {
    /*
     * @param A: An integer array
     * @param queries: The query list
     * @return: The number of element in the array that are smaller that the given integer
     */
    public List<Integer> countOfSmallerNumber(int[] A, int[] queries) {
        // write your code here
        // 14069 ms
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < queries.length; i++) {
            int target = queries[i];
            int count = 0;
            for (int a:A) { if (a < target) count++; }
            res.add(count);
        }
        return res;
    }

    public List<Integer> countOfSmallerNumber2(int[] A, int[] queries) {
        // write your code here
        // binary search
        // 7096 ms
        Arrays.sort(A);
        List<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0) {
            for (int i = 0; i < queries.length; i++) res.add(0);
            return res;
        }
        for (int i = 0; i < queries.length; i++) {
            int target = queries[i];
            int start = 0, end = A.length - 1;
            int mid;
            //Find the maximum i, s.t. A[i] < target
            while (start < end) {
                mid = start + ((end - start + 1) >> 1);
                if (A[mid] < target) start = mid;
                else end = mid - 1;
            }
            res.add((A[start] < target ? start:-1) + 1);
        }
        return res;
    }
}