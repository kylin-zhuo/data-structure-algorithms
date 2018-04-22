public class Solution {
    /*
     * @param A: Given an integer array
     * @return: nothing
     */
    public void heapify(int[] A) {
        // write your code here
        for(int i = A.length/2; i >= 0; i--) {
            heapify(A, i);
        }
    }
    
    void heapify(int[] A, int i) {
        int left = i * 2 + 1;
        int right = i * 2 + 2;
        int smallest = i;
        if (left < A.length && A[left] < A[smallest]) smallest = left;
        if (right < A.length && A[right] < A[smallest]) smallest = right;
        if (smallest != i) {
            swap(A, i, smallest);
            heapify(A, smallest);
        }
    }
    
    void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}