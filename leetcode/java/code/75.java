public class Solution {
    /*
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        if(A.length <= 1) return 0;
        int start = 0, end = A.length - 1;
        
        while(start < end - 1){
            int mid = start + (end - start) / 2;
            if(A[mid] > A[mid+1] && A[mid] > A[mid-1]) return mid;
            else if(A[mid] < A[mid+1]) start = mid;
            else end = mid;
        }
        return A[start] > A[end] ? start:end;
    }
}