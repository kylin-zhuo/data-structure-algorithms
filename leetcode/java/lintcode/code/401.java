public class Solution {
    /*
     * @param matrix: a matrix of integers
     * @param k: An integer
     * @return: the kth smallest number in the matrix
     */
    
    private class Wrapper {
        int val;
        int row;
        int col;
        Wrapper(int row, int col, int val) {
            this.row = row;
            this.col = col;
            this.val = val;
        }
    } 
    
    public int kthSmallest(int[][] matrix, int k) {
        // write your code here
        int m = matrix.length;
        int n = matrix[0].length;
        Queue<Wrapper> heap = new PriorityQueue<Wrapper>(11, new Comparator<Wrapper>() {
            public int compare(Wrapper w1, Wrapper w2) {
                if (w1.val < w2.val) return -1;
                else if (w1.val > w2.val) return 1;
                else return 0;
            }
        });
        for (int i = 0; i < m; i++) {
            heap.offer(new Wrapper(i, 0, matrix[i][0]));
        }
        for (int i = 0; i < k-1; i++) {
            Wrapper w = heap.poll();
            if (w.col < n - 1) heap.offer(new Wrapper(w.row, w.col+1, matrix[w.row][w.col+1]));
        }
        return heap.poll().val;
    }
}