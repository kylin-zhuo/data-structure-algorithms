public class Solution64 {
    /*
     * @param A: sorted integer array A which has m elements, but size of A is m+n
     * @param m: An integer
     * @param B: sorted integer array B which has n elements
     * @param n: An integer
     * @return: nothing
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here
        int ia = m - 1;
        int ib = n - 1;
        while (ia >= 0 && ib >= 0) {
            if (B[ib] >= A[ia]) {
                A[ia+ib+1] = B[ib];
                ib --;
            }
            else {
                swap(A, ia, ia+ib+1);
                ia --;
            }
        }
        if (ia < 0) {
            for (int k = ib; k >= 0; k--) A[k] = B[k];
        }
    }
    
    public void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}