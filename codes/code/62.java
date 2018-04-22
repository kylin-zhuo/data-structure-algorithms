public class Solution {
    /*
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        int left = 0;
        int right = A.length - 1;
        int mid;
        
        while (left <= right) {
            mid = (left + right) / 2;
            if (A[mid] == target) return mid;
            if (A[left] <= A[mid]) {
                if (target < A[mid] && target >= A[left]) right = mid - 1;
                else left = mid + 1;
            }
            if (A[right] >= A[mid]) {
                if (target > A[mid] && target <= A[right]) left = mid + 1;
                else right = mid - 1;
            }
        }
        return -1;
    }
    
}